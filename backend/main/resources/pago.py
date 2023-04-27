from flask_restful import Resource
from flask import abort
from main.models import PagosModelo, UsuarioModelo
from .. import db


class Pago(Resource):

    def get(self, user_id):
        try:
            rescate_pago = db.session.query(PagosModelo).filter(
                PagosModelo.dni == user_id
            ).firts()
            return rescate_pago.to_json(), 201

        except BaseException:
            abort(404, 'No se ha encontrado pagos del alumnmo')

        finally:
            db.session.close()

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
