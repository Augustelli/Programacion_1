from flask_restful import Resource
from .. import db
from main.models import ClasesModelo
from flask import abort


class ProfesorClases(Resource):
    def get(self):
        try:
            clases = db.session.query(ClasesModelo).all()
            return clases.to_json()
        except Exception:
            abort(404, 'No se ha encontrado las clases.')
        finally:
            db.session.close()
