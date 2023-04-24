from flask_restful import Resource
from flask import request, abort
from .. import db
from main.models import Planificaciones_UsuarioModelo, PlanificacionModelo    


class PlanificacionAlumno(Resource):

    def get(self, user_id):
        try:
            planificacion = db.session.query(Planificaciones_UsuarioModelo).filter(Planificaciones_UsuarioModelo.idUsuario).all()
            return planificacion.to_json()

        except BaseException:
            abort(404, f'Planificaciones del usuario {user_id} no encontradas')
        finally:
            db.session.close()


class PlanificacionProfesor(Resource):

    def get(self, user_id):
        try:
            planificacion = db.session.query(PlanificacionModelo).filter(PlanificacionModelo.idPlanificacion).all()
            return planificacion.to_json()

        except BaseException:
            abort(404, f'Planificaciones del Profesor {user_id} no encontradas')
        finally:
            db.session.close()

    def delete(self, user_id, idplanificacion):
        try:
            planificacion_eliminar = db.session.query(PlanificacionModelo).filter(
                PlanificacionModelo.idPlanificacion == idplanificacion,
                PlanificacionModelo.idUsuario == user_id)
            db.session.delete(planificacion_eliminar)
            db.session.commit()
        except BaseException:
            abort(404, 'No se ha encontrado la planificación del alumno.')
        finally:
            db.session.close()

    def put(self, user_id, idplanificacion):

        try:
            planificacion_editar = db.session.query(PlanificacionModelo).filter(
                PlanificacionModelo.idPlanificacion == idplanificacion,
                PlanificacionModelo.idUsuario == user_id
            ).first()
            informacion = request.get_json().items()
            for campo, valor in informacion:
                setattr(planificacion_editar, campo, valor)
            db.session.add(planificacion_editar)
            db.sessio.commit()
        except BaseException:
            abort(422, 'No se ha podido realizar el cambio.')
        finally:
            db.session.close()


class PlanificacionesProfesores(Resource):

    def get(self):
        try:
            planificaciones = db.session.query(PlanificacionModelo).all()
            return planificaciones.to_json()
        except Exception:
            abort(404, 'No se han encontrado las planificaciones.')
        finally:
            db.session.commit()

    def post(self):
        try:
            planificacion_nueva = PlanificacionModelo.from_json(request.get_json())
            db.session.add(planificacion_nueva)
            db.session.commit()
            return planificacion_nueva.to_json()
        except BaseException:
            abort(404, 'Error al crear el usuario')
        finally:
            db.session.close()
