from flask import request, abort, jsonify
from .. import db
from main.models import ClasesModelo
from flask_restful import Resource


class Clases_R(Resource):

    ###NO FUNCIONAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    def get(self):
        try:
            clase = db.session.query(ClasesModelo).filter().all()
            lista_clases = [clase.to_json() for clase in clase]
            return jsonify(lista_clases),201
        except BaseException:
            abort(404, 'No se ha encontrado la Clase')
        finally:
            db.session.close()

#     def post(self):
#         try:
#             datos = request.get_json()
#             clase_nueva = ClasesModelo.from_json(datos)
#             db.session.add()
#             db.session.commit()
#             return clase_nueva.to_json(), 201
#         except BaseException:
#             abort(404, 'Error al crear la clase')
#         finally:
#             db.session.close()


class Clase_R(Resource):

    def delete(self, user_id):
        #try:
            clase_eliminar = db.session.query(ClasesModelo).filter(
                ClasesModelo.idClases == user_id).first()
            db.session.delete(clase_eliminar)
            db.session.commit()
            return 204
        # except BaseException:
        #     abort(404, 'No se ha encontrado la clase {}'.format(user_id))
        # finally:
        #     db.session.close()

             

    # def delete(self, user_id):
    #     '''DELETE -> Rol Admin, Profesor'''
    #     try:
    #         profe_eliminar = db.session.query(ProfesorModelo).filter(or_(
    #                 ProfesorModelo.profesor_dni == user_id,
    #                 ProfesorModelo.idProfesor == user_id
    #             )).first()
    #         db.session.delete(profe_eliminar)
    #         db.session.commit()
    #         return 204
    #     except BaseException:
    #         abort(404, 'No se ha encontrado el alumno de id {}'.format(user_id))
    #     finally:
    #         db.session.close()


#     def get(self, idclase):
#         try:
#             clase = db.session.query(ClasesModelo).filter(
#                 ClasesModelo.idClases == idclase
#             ).first()
#             return clase.to_json(), 201
#         except BaseException:
#             abort(404, 'No se ha encontrado la Clase')
#         finally:
#             db.session.close()
