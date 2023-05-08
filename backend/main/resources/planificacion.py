from flask_restful import Resource
from flask import request, abort, jsonify
from .. import db
from main.models import PlanificacionModelo, AlumnoModel
import pdb


class PlanificacionAlumno(Resource):

    def get(self):
        try:
            page = 1
            per_page = 10
            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))

            if request.args.get('nrIdAlumno'):
                planificacion = db.session.query(PlanificacionModelo).filter(
                    PlanificacionModelo.id_Alumno == int(request.args.get('nrIdAlumno'))
                    ).order_by(PlanificacionModelo.fecha.desc()).all()
            elif request.args.get('nrDniAlumno'):
                planificacion = db.session.query(PlanificacionModelo).join().filter(
                    AlumnoModel.alumno_dni == int(request.args.get('nrDniAlumno'))
                ).order_by(PlanificacionModelo.fecha.desc()).all()
            else:
                raise Exception('Se debe indicar el Id del alumno o su DNI.')

            planificacion = planificacion.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            planificacion_json = [planificacion.to_json() for planificacion in planificacion]
            return jsonify({'Usuario': planificacion_json,
                            'Pagina': page,
                            'Por pagina': per_page,
                            'Total': planificacion.total,
                            })
        except Exception:
            abort(404, f"Planificaciones del usuario {request.args.get('nrIdAlumno'),request.args.get('nrDniAlumno') } no encontradas")
        finally:
            db.session.close()


class PlanificacionesProfesores(Resource):

    def get(self):
        try:
            planificacion = db.session.query(PlanificacionModelo)
            page = 1
            per_page = 10

            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            # Si manda DNI, le va a mostrar Todas , si manda id Planificacion 1 y si manda idAlumno la más reciente
            # Si no hay argumentos, listará todas las planificaciones
            if request.args.get('nrDni'):
                planificacion = planificacion.outerjoin(
                    AlumnoModel, AlumnoModel.idAlumno == PlanificacionModelo.id_Alumno).filter(
                    AlumnoModel.alumno_dni == int(request.args.get('nrDni'))
                ).order_by(PlanificacionModelo.fecha.desc())
            
            elif request.args.get('nrIdPlanificacion'):
                planificacion = planificacion.filter(
                    PlanificacionModelo.idPlanificacion == int(request.args.get('nrIdPlanificacion'))
                ).order_by(PlanificacionModelo.fecha.desc())
            
            elif request.args.get('nrIdAlumno'):
                planificacion = db.session.query(PlanificacionModelo).filter(
                    PlanificacionModelo.id_Alumno == int(request.args.get('nrIdAlumno'))
                    ).order_by(PlanificacionModelo.fecha.desc())
            
            planificacion_paginados = planificacion.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            planificacion_json = [planificacion.to_json() for planificacion in planificacion_paginados.items]
            # return jsonify(planificacion_json)
            return jsonify({'Usuario': planificacion_json,
                            'Pagina': page,
                            'Por pagina': per_page,
                            'Total': planificacion_paginados.total
                            })
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

    def delete(self):
        try:
            planificacion = db.session.query(PlanificacionModelo)

            if request.args.get('nrIdPlanificacion'):
                #usuario_id = int(request.args.get('nrIdAlumno'))
                if request.args.get('nrIdAlumno'):
                # Verifica si la planificación pertenece al alumno
                    
                    planificacion = planificacion.filter(
                        planificacion.idPlanificacion == int(request.args.get('nrIdPlanificacion')),
                        planificacion.id_Alumno == int(request.args.get('nrIdAlumno')))
                    
                    if planificacion:
                        pdb.set_trace()
                        db.session.delete(planificacion)
                        db.session.commit()
                        return 204
                else:
                    raise Exception('La planificación no coincide con una asociada al Alumno.')
            else:
                raise Exception('Se debe proveer con el identenficador de la Planificación para eliminarla ')
        except Exception:
            abort(404, f"No se ha encontrado la planificación  de id {request.args.get('nrIdPlanificacion')}")
        finally:
            db.session.close()

    def put(self):

        try:
            if request.args.get('nrIdPlanificacion'):
                usuario_id = int(request.args.get('nrIdAlumno'))
                # Verifica si la planificación pertenece al alumno
                planificacion = db.session.query(PlanificacionModelo).filter(
                   PlanificacionModelo.idPlanificacion == int(request.args.get('nrIdPlanificacion')),
                   PlanificacionModelo.id_Alumno == usuario_id).first()
                if planificacion:
                    informacion = request.get_json().items()
                    for campo, valor in informacion:
                        setattr(planificacion, campo, valor)
                    db.session.add(planificacion)
                    db.session.commit()
                    return planificacion.to_json(), 201
                else:
                    raise Exception('La planificación a editar no pertenece al usuario')
            else:
                raise Exception('Debe brindarse el identificador de la planificaicion')
        except BaseException:
            abort(422, 'No se ha podido realizar el cambio.')
        finally:
            db.session.close()

    def post(self):
        try:
            # Se supone que puede haber rutinas que no pertenezcan a ninguna clase
            campos_obligatorios = {'rutina', 'id_Alumno', 'idProfesor'}
            datos = request.get_json()
            campos_recibidos = set(datos.keys())

            campos_faltantes = campos_obligatorios - campos_recibidos
            if campos_faltantes:
                raise Exception(f'Error al crear la rutina. Faltan campos obligatorios: {campos_faltantes}. Por favor, incluya estos campos y vuelva a intentarlo.')  # noqa

            for campo in campos_obligatorios:
                if datos[campo] is None:
                    raise Exception(f'Error al crear rutina. El campo {campo} no puede ser nulo. Por favor, proporcione un valor válido para {campo} y vuelva a intentarlo.')  # noqa:
            planificacion_nueva = PlanificacionModelo.from_json(datos)
            db.session.add(planificacion_nueva)
            db.session.commit()
            return planificacion_nueva.to_json(), 201
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

# Este recurso se tiene que ir (SOLO QUEDA EL RECURSO DE PLANIFICACIONESPROFESORES Y PLANIFICACIONESALUMNO)
