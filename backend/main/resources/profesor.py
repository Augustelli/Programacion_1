from flask_restful import Resource
from .. import db
from main.models import ProfesorModelo
from flask import abort,request,jsonify  # noqa


class ProfesorClases(Resource):
    def get(self):
        try:
            clases = db.session.query(ProfesorModelo).all()
            return clases.to_json()
        except Exception:
            abort(404, 'No se ha encontrado los profesores')
        finally:
            db.session.close()
