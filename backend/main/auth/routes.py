from flask import request, Blueprint
from .. import db
from main.models import UsuarioModelo, AlumnoModel, Login_usuarioModelo
from flask_jwt_extended import create_access_token
import pdb  # noqa
from main.mail.functions import sendMail
import time
import hashlib
from datetime import datetime


# Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')


# Método de logueo
@auth.route('/login', methods=['POST'])
def login():
    try:
        usuario = db.session.query(UsuarioModelo).filter(UsuarioModelo.email == request.get_json().get("email")).first_or_404()

        # Valida la contraseña
        if usuario.validate_pass(request.get_json().get("contrasegna")):
            # Genera un nuevo token
            # Pasa el objeto usuario como identidad
            data = request.get_json()
            access_token = create_access_token(identity=usuario)
            login_data = f"{usuario.email}-{data.get('contrasegna')}-{datetime.now()}-".encode('utf-8')
            hash_calculado = hashlib.sha256(login_data).hexdigest()

            # Devolver valores y token
            data = {
                'dni': str(usuario.dni),
                'email': usuario.email,
                'access_token': access_token
            }
            registro_login = Login_usuarioModelo(
                nombre_usuario = usuario.nombre_usuario,
                fecha_login = datetime.now(),
                hash_datos = hash_calculado
            )
            db.session.add(registro_login)
            db.session.commit()
            return data, 200
        else:
            return 'Contraseña incorrecta', 401
    except Exception as e:
        return e
    finally:
        db.session.close()
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

            datos['rol'] = "espera"
            usuario_nuevo = UsuarioModelo.from_json(datos)
            db.session.add(usuario_nuevo)
            alumno = AlumnoModel(
                alumno_dni=usuario_nuevo.dni,
                altura=datos['altura'] if 'altura' in datos else None,
                peso=datos['peso'] if 'peso' in datos else None
                )
            db.session.add(alumno)
            db.session.commit()
            # Enviar mail de Bienvenida
            _ = sendMail([usuario_nuevo.email], "Bienvenido a la plataforma del gimnasio del Grupo D", "register", usuario=usuario_nuevo)
            return usuario_nuevo.to_json(), 201
        except Exception as e:
            db.session.rollback()
            return {'Error': str(e)}, 400
        finally:
            db.session.close()
