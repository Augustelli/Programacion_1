from flask_restful import Resource
from .. import db
from main.models import ClaseModelo
from flask import abort


class ProfesorClases(Resource):
    def get(self, user_id):
        try:
            clases = db.session.query(ClaseModelo).all()
            return clases.to_json()
        except Exception:
            abort(404, 'No se ha encontrado las clases.')
        finally:
            db.session.close()
