from flask_restful import Resource
from flask import abort, request, jsonify
from main.models import PagosModelo, UsuarioModelo
from .. import db


class Pago(Resource):

    def get(self, user_id):
        #try:
            rescate_pago = db.session.query(PagosModelo).filter(
                PagosModelo.dni == user_id
            ).first()
            return rescate_pago.to_json(), 201

        # except BaseException:
        #     abort(404, 'No se ha encontrado pagos del alumnmo')

        # finally:
        #     db.session.close()

        
        #   def get(self, user_id):
        # try:
        #     usuario_rescatado = db.session.query(UsuarioModelo).filter(
        #         UsuarioModelo.dni == user_id).first()
        #     return usuario_rescatado.to_json(), 201
        # except Exception:
        #     abort(404, f'No se ha encontrado del usuario de id: {user_id}')
        # finally:




    def put(self, user_id):
        try:
            pago = db.session.query(PagosModelo).filter(PagosModelo.dni == user_id).order_by(PagosModelo.estado.asc()).all()
            pago.estado = "No pagado" if pago.estado == "Pagado" else "Pagado"
            usuario = db.session.query(UsuarioModelo).filter_by(UsuarioModelo.dni == user_id).first()
            usuario.estado = pago.estado
            db.session.commit()
        except Exception:
            abort(404, f'No se pudo realizar la actualización del estado. Usuario id {user_id}')
        finally:
            db.session.close()

    def delete(self, user_id):
        try:
            pago_eliminar = db.session.query(PagosModelo).filter(PagosModelo.dni == user_id).first()
            db.session.delete(pago_eliminar)
            db.session.commit()
            return 204
        except BaseException:
            abort(404, 'No se ha encontrado el pago del alumno de id {}'.format(user_id))
        finally:
            db.session.close()


class Pagos(Resource):



    def post(self):
        try:
            dato_nuevo=PagosModelo.from_json(request.get_json())
            db.session.add(dato_nuevo)
            db.session.commit()
            return dato_nuevo.to_json(), 201
        except BaseException:
            abort(404, 'Error al crear el Pago')
        finally:
            db.session.close()


    def get(self):
        try:
            pagos = db.session.query(PagosModelo).all
            pagos_json = [pago.to_json() for pago in pagos]
            return jsonify(pagos_json)
        except Exception:
            abort(404, 'No se ha podido realizar la consulta')
        finally:
            db.session.close()



    



            
