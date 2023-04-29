from flask_restful import Resource
from .. import db
from main.models import ClaseModelo
from flask import abort


class ProfesorClases(Resource):
    def get(self):
        try:
            clases = db.session.query(ClaseModelo).all()
            return clases.to_json()
        except Exception:
            abort(404, 'No se ha encontrado las clases.')
        finally:
            db.session.close()

class Profesor(Resource):
    def get(self):
        try:
            profesores = db.session.query(ProfesorModelo).all()
            return profesores.to_json()
        except Exception:
            abort(404, 'No se ha encontrado los profesores.')
        finally:
            db.session.close()
    
    def post(self):
        try:
            profesor = ProfesorModelo.from_json(request.json)
            db.session.add(profesor)
            db.session.commit()
        except Exception:
            abort(404, 'Error al crear el profesor.')
        finally:
            db.session.close()
            
