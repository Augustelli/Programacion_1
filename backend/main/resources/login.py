from flask_restful import Resource
from flask import request, abort
from .. import db
from main.models import UsuarioModelo


class Login(Resource):

    #  def post(self):
    #     try:
    #         usuario_nuevo = UsuarioModelo.from_json(request.get_json())
    #         db.session.add(usuario_nuevo)
    #         db.session.commit()
    #         return usuario_nuevo.to_json(), 201
    #     except BaseException:
    #         abort(404, 'Error al crear el usuario')
    #     finally:
    #         db.session.close()

    def post(self):
        try:
            info = request.get_json()
            print(info)
            usuario = info['nombre_usuario']

            contrasegna = info['contrasegna']

            query = db.session.query(UsuarioModelo).filter(UsuarioModelo.nombre_usuario == usuario).first()
            if query.contrasegna == contrasegna:
                return 201
            else:
                return 403
        except BaseException:
            abort(404, 'Error al crear el usuario')
        finally:
            db.session.close()
    # def post(self):
    #     try:
    #         informacion = request.get_json()
    #         info_validar = db.session.query(UsuarioModelo).filter(
    #             Usuario_contrasegnaModelo.nombre_usuario == informacion.json['nombre_usuario']
    #         )
    #         if info_validar.contrasegna_hash == hashlib.sha256(informacion.json['contrasegna_hash'].encode('utf-8')).hexdigest():
    #             log_in = Login_usuarioModelo(
    #                 nombre_usuario=informacion.json['nombre_usuario'])
    #             db.session.add(log_in)
    #             db.session.commit()
    #     except BaseException:
    #         abort(404, 'Error al crear el log in')
    #     finally:
    #         db.session.close()
