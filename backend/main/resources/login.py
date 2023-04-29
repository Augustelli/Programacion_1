from flask_restful import Resource
from flask import request, abort
from .. import db
from main.models import Usuario_ContrasegnaModelo, Login_usuarioModelo
import hashlib


class Login(Resource):

    def post(self):
        try:
            informacion = request.get_json()
            info_validar = db.session.query(Usuario_ContrasegnaModelo).filter(
                Usuario_ContrasegnaModelo.nombre_usuario == informacion.json['nombre_usuario']
            )
            if info_validar.contrasegna_hash == hashlib.sha256(informacion.json['contrasegna_hash'].encode('utf-8')).hexdigest():
                log_in = Login_usuarioModelo(
                    nombre_usuario=informacion.json['nombre_usuario'])
                db.session.add(log_in)
                db.session.commit()
        except BaseException:
            abort(404, 'Error al crear el log in')
        finally:
            db.session.close()
