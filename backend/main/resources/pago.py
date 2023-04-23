from flask_restful import Resource
from flask import abort
from main.models import PagosModelo
from main import db


class Pago(Resource):

    def get(self, user_id):
        try:
            rescate_pago = db.session.query(PagosModelo).filter(PagosModelo.idUsuario == user_id ).firts()
            return rescate_pago.to_json(), 201

        except BaseException:
            abort(404, 'No se ha encontrado pagos del alumnmo')

        finally:
            db.session.close()

    def put(self, user_id)
