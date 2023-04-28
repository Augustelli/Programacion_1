from flask import request, abort
from .. import db
from main.models import ClasesModelo


class Clases_R(db.Model):

    def get(self):
        try:
            clase = db.session.query(ClasesModelo).filter().all()
            return clase.to_json(), 201
        except BaseException:
            abort(404, 'No se ha encontrado la Clase')
        finally:
            db.session.close()

    def post(self):
        try:
            datos = request.get_json()
            clase_nueva = ClasesModelo.from_json(datos)
            db.session.add()
            db.session.commit()
            return clase_nueva.to_json(), 201
        except BaseException:
            abort(404, 'Error al crear la clase')
        finally:
            db.session.close()


class Clase_R(db.Model):

    def delete(self, idclase):
        try:
            clase_eliminar = db.session.query(ClasesModelo).filter(
                ClasesModelo == idclase).first()
            db.session.delete(clase_eliminar)
            db.session.commit()
            return 204
        except BaseException:
            abort(404, 'No se ha encontrado la clase {}'.format(idclase))
        finally:
            db.session.close()

    def get(self, idclase):
        try:
            clase = db.session.query(ClasesModelo).filter(
                ClasesModelo.idClases == idclase
            ).first()
            return clase.to_json(), 201
        except BaseException:
            abort(404, 'No se ha encontrado la Clase')
        finally:
            db.session.close()
