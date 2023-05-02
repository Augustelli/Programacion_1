from flask_restful import Resource
from flask import request, abort, jsonify
from .. import db
from main.models import PlanificacionModelo


class PlanificacionAlumno(Resource):

    def get(self, user_id):
        try:
            planificacion = db.session.query(PlanificacionModelo).filter(PlanificacionModelo.id_Alumno == user_id).all()
            planificacion_json = [planificacion.to_json() for planificacion in planificacion]
            return jsonify(planificacion_json)

        except BaseException:
            abort(404, f'Planificaciones del usuario {user_id} no encontradas')
        finally:
            db.session.close()

 

class PlanificacionProfesor(Resource):

    def get(self, user_id):
        try:
            planificacion = db.session.query(PlanificacionModelo).filter(PlanificacionModelo.idProfesor == user_id).all()
            planificacion_json = [planificacion.to_json() for planificacion in planificacion]
            return jsonify(planificacion_json)

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

        #try:
            planificacion_editar = db.session.query(PlanificacionModelo).filter(
                PlanificacionModelo.idPlanificacion == user_id,
            ).first()
            informacion = request.get_json().items()
            for campo, valor in informacion:
                setattr(planificacion_editar, campo, valor)
            db.session.add(planificacion_editar)
            db.session.commit()
            return planificacion_editar.to_json(), 201
        # except BaseException:
        #     abort(422, 'No se ha podido realizar el cambio.')
        # finally:
        #     db.session.close()


class PlanificacionesProfesores(Resource):

    def get(self):
        try:
            planificaciones = db.session.query(PlanificacionModelo).all()
            planificaciones_json = [planificacion.to_json() for planificacion in planificaciones]
            return jsonify(planificaciones_json)
           
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
            abort(404, 'Error al crear la planificación')
        finally:
            db.session.close()

