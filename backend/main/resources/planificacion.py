from flask_restful import Resource
from flask import request, abort, jsonify
from .. import db
from main.models import PlanificacionModelo, ProfesorModelo 


class PlanificacionAlumno(Resource):

    def get(self, user_id):
        try:
            planificacion = db.session.query(PlanificacionModelo).filter(PlanificacionModelo.id_Alumno == user_id)
            page = 1
            per_page = 10
            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            planificacion = planificacion.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            planificacion_json = [planificacion.to_json() for planificacion in planificacion]
            return jsonify({'Usuario': planificacion_json,
                            'Pagina': page,
                            'Por pagina': per_page,
                            'Total': planificacion.total,
                            })
        except BaseException:
            abort(404, f'Planificaciones del usuario {user_id} no encontradas')
        finally:
            db.session.close()


class PlanificacionProfesor(Resource):

    def get(self, user_id):
        try:
            planificacion = db.session.query(PlanificacionModelo).filter(PlanificacionModelo.idProfesor == user_id)
            page = 1
            per_page = 10
            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            


            planificacion = planificacion.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            planificacion_json = [planificacion.to_json() for planificacion in planificacion]
            # return jsonify(planificacion_json)
            return jsonify({'Usuario': planificacion_json,
                            'Pagina': page,
                            'Por pagina': per_page,
                            'Total': planificacion.total,
                            })
        except BaseException:
            abort(404, f'Planificaciones del usuario {user_id} no encontradas')
        finally:
            db.session.close()

    def delete(self, user_id):
        try:
            planificacion_eliminar = db.session.query(PlanificacionModelo).filter(
                PlanificacionModelo.idPlanificacion == user_id).first()
            db.session.delete(planificacion_eliminar)
            db.session.commit()
            return 204
        except BaseException:
            abort(404, f'No se ha encontrado la planificación  de id {user_id}')
        finally:
            db.session.close()

    def put(self, user_id):

        try:
            planificacion_editar = db.session.query(PlanificacionModelo).filter(
                PlanificacionModelo.idPlanificacion == user_id,
            ).first()
            informacion = request.get_json().items()
            for campo, valor in informacion:
                setattr(planificacion_editar, campo, valor)
            db.session.add(planificacion_editar)
            db.session.commit()
            return planificacion_editar.to_json(), 201
        except BaseException:
            abort(422, 'No se ha podido realizar el cambio.')
        finally:
            db.session.close()


class PlanificacionesProfesores(Resource):

    def get(self):
        # try:
            planificaciones=db.session.query(PlanificacionModelo)
            if request.args.get('nrProfe'):
                planificaciones=planificaciones.outerjoin(ProfesorModelo.idProfesor).group_by(ProfesorModelo.idProfesor).having(ProfesorModelo.idProfesor == request.args.get('nrProfe'))

            if request.args.get('nrRutina'):
                planificaciones=planificaciones.filter(PlanificacionModelo.rutina.like("%"+request.args.get('nrRutina')+"%"))

            if request.args.get('nrRutinas'):
                planificaciones=planificaciones.filter(PlanificacionModelo.rutina)
            #if request.args.get('')
            #planificaciones = db.session.query(PlanificacionModelo)
            page = 1
            per_page = 10
            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            planificaciones = planificaciones.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            planificaciones_json = [planificacion.to_json() for planificacion in planificaciones]
            # return jsonify(planificaciones_json)
            return jsonify({'Planificaciones': planificaciones_json,
                            'Pagina': page,
                            'Por pagina': per_page,
                            'Total': planificaciones.total,
                            })

        # except Exception:
        #     abort(404, 'No se han encontrado las planificaciones.')
        # finally:
        #     db.session.commit()

    def post(self):
        try:
            planificacion_nueva = PlanificacionModelo.from_json(request.get_json())
            db.session.add(planificacion_nueva)
            db.session.commit()
            return planificacion_nueva.to_json()
        except BaseException:
            abort(404, 'Error al crear la planificación')
        finally:
            db.session.close()
