from flask import request, Blueprint
from .. import db
from main.models import UsuarioModelo, AlumnoModel
from flask_jwt_extended import create_access_token
import pdb  # noqa
from main.mail.functions import sendMail

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
            'dni': str(usuario.dni),
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
    email_nuevo = request.get_json()['email']  # noqa

    correo_existente = db.session.query(UsuarioModelo).filter(UsuarioModelo.email == email_nuevo).first()
    if correo_existente:
        return 'Duplicated mail', 409
    else:
        try:
            campos_obligatorios = {'dni', 'nombre', 'apellido', 'email', 'contrasegna'}
            datos = request.get_json()
            campos_recibidos = set(datos.keys())

            campos_faltantes = campos_obligatorios - campos_recibidos
            if campos_faltantes:
                raise Exception(
                    f'Error al crear usuario. Faltan campos obligatorios: {campos_faltantes}. Por favor, incluya estos campos y vuelva a intentarlo.')

            for campo in campos_obligatorios:
                if datos[campo] is None:
                    raise Exception(f'Error al crear usuario. El campo {campo} no puede ser nulo. Por favor, proporcione un valor válido para {campo} y vuelva a intentarlo.')  # noqa

            datos['rol'] = "alumno"
            usuario_nuevo = UsuarioModelo.from_json(datos)
            db.session.add(usuario_nuevo)
            alumno = AlumnoModel(alumno_dni=usuario_nuevo.dni)
            db.session.add(alumno)
            db.session.commit()
            # Enviar mail de Bienvenida
            sent = sendMail([usuario_nuevo.email], "Bienvenido a la plataforma del gimnasio del Grupo D", "register", usuario=usuario_nuevo)  # noqa
            return usuario_nuevo.to_json(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
        finally:
            db.session.close()
