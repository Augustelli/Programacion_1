from flask_restful import Resource
from flask import request, abort, jsonify
from .. import db
from main.models import PlanificacionModelo, AlumnoModel, UsuarioModelo,PlanificacionDetalleModelo
from flask_jwt_extended import jwt_required, get_jwt_identity  # noqa
from main.auth.decorators import role_required
import pdb  # noqa
from main.mail.functions import sendMail


class PlanificacionesDetalle(Resource):
    # @role_required(roles=['admin', 'profesor', 'alumno'])
    def get(self):
        try:
            page = 1
            per_page = 10

            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            planificaciondetalle = db.session.query(PlanificacionDetalleModelo)


            planificaciondetalle_paginados = planificaciondetalle.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)


            planificaciondetalle_json = [planificaciondetalle.to_json() for planificaciondetalle in planificaciondetalle_paginados.items]
            return {
                'PlanificacionDetalle': planificaciondetalle_json,
                'Pagina': page,
                'Por pagina': per_page,
                'Total': planificaciondetalle_paginados.total
                }

        except Exception as e:
            return {'error': str(e)}, 404
        finally:
            db.session.close()

    
    # @role_required(roles=['admin', 'profesor', 'alumno'])
    def post(self):
        try:
            campos_obligatorios = {'idPlanificacion', 'nombre'}
            datos = request.get_json()
            campos_recibidos = set(datos.keys())

            campos_faltantes = campos_obligatorios - campos_recibidos
            if campos_faltantes:
                raise Exception(
                    f'Error al crear alumno. Faltan campos obligatorios: {campos_faltantes}. Por favor, incluya estos campos y vuelva a intentarlo.')

            for campo in campos_obligatorios:
                if datos[campo] is None:
                    raise Exception(
                        f'Error al crear alumno. El campo {campo} no puede ser nulo. Por favor, proporcione un valor válido para {campo} y vuelva a intentarlo.')  # noqa

            planificaciondetallenueva = PlanificacionDetalleModelo.from_json(datos)
            db.session.add(planificaciondetallenueva)
            db.session.commit()
            return planificaciondetallenueva.to_json(), 201
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

   




class PlanificacionDetalle(Resource):


    # @role_required(roles=['admin', 'profesor', 'alumno'])
    
    def get(self):
        try:
            planificaciondetalle = db.session.query(PlanificacionDetalleModelo)
            plani=db.session.query(PlanificacionModelo)
            page = 1
            per_page = 10

            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            # Si manda DNI, le va a mostrar Todas , si manda id planificaciondetalle 1 y si manda idAlumno la más reciente
            # Si no hay argumentos, listará todas las planificaciondetallees
            

            if request.args.get('idPlanificacion'):
                planificaciondetalle = planificaciondetalle.filter(PlanificacionDetalleModelo.idPlanificacion == request.args.get('idPlanificacion'))
                plani=plani.filter(PlanificacionModelo.idPlanificacion == request.args.get('idPlanificacion'))

            
            
           
                

          
            planificacion_paginados = planificaciondetalle.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            planificacion_json = [planificaciondetalle.to_json() for planificaciondetalle in planificacion_paginados.items]

            # return jsonify(planificacion_json)
            return jsonify({'Planificacion': planificacion_json,
                            'Pagina': page,
                            'Por pagina': per_page,
                            'Total': planificacion_paginados.total
                            })
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()


    def put(self):
        try:
            if request.args.get('idPlanificacionDetalle'):
                registro = db.session.query(PlanificacionDetalleModelo).get(request.args.get('idPlanificacionDetalle'))
                if registro:
                    pass
                else:
                    raise Exception(f"No se ha encontrado planificacion con esa ID: {(request.args.get('idPlanificacionDetalle'))}")
                detalle_editado = db.session.query(PlanificacionDetalleModelo).filter(PlanificacionDetalleModelo.idPlanificacionDetalle == int(request.args.get('idPlanificacionDetalle'))).first()  # noqa
                informacion = request.get_json().items()
                for campo, valor in informacion:
                    setattr(detalle_editado, campo, valor)
                db.session.add(detalle_editado)
                db.session.commit()
                return detalle_editado.to_json(), 201
            else:
                raise Exception('Es necesario el ID de la planificacion para modificar.')
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()
    
    def delete(self):
        try:
            if request.args.get('idPlanificacionDetalle'):
                registro = db.session.query(PlanificacionDetalleModelo).get(request.args.get('idPlanificacionDetalle'))
                print(registro)
                if registro:
                    pass
                else:
                    raise Exception(f'No se ha encontrado la planificacion por su ID')

                detalle_eliminar = db.session.query(PlanificacionDetalleModelo).filter(PlanificacionDetalleModelo.idPlanificacionDetalle == request.args.get('idPlanificacionDetalle')).first()  # noqa
                db.session.delete(detalle_eliminar)
                db.session.commit()
                # return 'Usuario eliminado correctamente', 200
                return 'Planificacion eliminada correctamente', 204
            else:
                raise Exception(f'Es necesario el ID de la planificacion para eliminarlo.')
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()
        
    

