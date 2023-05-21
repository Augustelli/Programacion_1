from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuarioModelo
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

# Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')


# Método de logueo
@auth.route('/login', methods=['POST'])
def login():
    # Busca al animal en la db por mail
    usuario = db.session.query(UsuarioModelo).filter(UsuarioModelo.email == request.get_json().get("email")).first_or_404()
    # Valida la contraseña
    if usuario.validate_pass(request.get_json().get("contrasegna")):
        # Genera un nuevo token
        # Pasa el objeto usuario como identidad
        access_token = create_access_token(identity=usuario)
        # Devolver valores y token
        data = {
            'id': str(usuario.id),
            'email': usuario.email,
            'access_token': access_token
        }

        return data, 200
    else:
        return 'Incorrect password', 401


# Método de registro
@auth.route('/register', methods=['POST'])
def register():
    usuario_nuevo = UsuarioModelo.from_json(request.get_json())
    # Verificar si el mail ya existe en la db
    exists = db.session.query(UsuarioModelo).filter(UsuarioModelo.email == usuario_nuevo.email).scalar() is not None
    if exists:
        return 'Duplicated mail', 409
    else:
        try:
            db.session.add(usuario_nuevo)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario_nuevo.to_json(), 201
