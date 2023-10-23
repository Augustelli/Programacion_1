from .. import db
from datetime import datetime
# from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
import os


def same_as(column_name):
    def default_function(context):
        return str(context.current_parameters.get(column_name))
    return default_function


class Usuario(db.Model):

    __tablename__ = 'usuario'

    dni = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    estado = db.Column(db.Boolean, default=False)
    rol = db.Column(db.String(10), default="alumno")
    nombre_usuario = db.Column(db.String(12), default=same_as('dni'), unique=True)
    contrasegna = db.Column(db.String(128), nullable=False)

    # Definimos la relación uno a uno con la tabla Alumno
    alumno = db.relationship('Alumno', back_populates='usuario', uselist=False,cascade='all, delete-orphan')
    profesor = db.relationship('Profesor', back_populates='usuario', uselist=False,cascade='all, delete-orphan')
    usuario_pagos = db.relationship('Pagos', back_populates='pagos_usuario', cascade='all, delete-orphan', single_parent=True)
    login1 = db.relationship('Login_usuario', back_populates='usuario', uselist=False)

    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')

    @plain_password.setter
    def plain_password(self, password):
        if password is not None and password.strip():
            self.contrasegna = generate_password_hash(password)

    def validate_pass(self, password):
        return check_password_hash(self.contrasegna, password)

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)
        if self.rol is None:
            self.rol = 'alumno'
        elif (self.dni == os.getenv('ADMIN_DNI')) and \
            (self.nombre_usuario == os.getenv('ADMIN_USERNAME')and \
                self.email == os.getenv('ADMIN_EMAIL')):
            self.rol = 'admin'

    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    # Setter de la contraseña toma un valor en texto plano
    # calcula el hash y lo guarda en el atributo password

    @plain_password.setter
    def plain_password(self, password):
        self.contrasegna = generate_password_hash(password)

    # Método que compara una contraseña en texto plano con el hash guardado en la db

    def validate_pass(self, password):
        return check_password_hash(self.contrasegna, password)

    def __repr__(self):
        return f'<Usuario: {self.nombre} {self.apellido} {self.estado}>'

    def to_json(self):

        usuario_json = {
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            # 'fecha_nacimiento': str(datetime.strptime(self.fecha_nacimiento) , '%Y-%m-%d'),
            # 'fecha_nacimiento': str(self.fecha_nacimiento.strftime( '%Y-%m-%d')),
            'fecha_nacimiento': str(self.fecha_nacimiento.strftime( '%d-%m-%Y')),
            'estado': self.estado,
            'rol': self.rol,
            'nombre_usuario': self.nombre_usuario
            # 'contrasegna': self.contrasegna,
            # 'altura': self.altura,
            # 'peso': self.peso
        }
        return usuario_json

    def to_json_complete(self):
        usuario_json = {
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'fecha_nacimiento': str((self.fecha_nacimiento.strftime( '%d-%m-%Y'))),
            # 'fecha_nacimiento': str((self.fecha_nacimiento.strftime( '%Y-%m-%d'))),
            'estado': self.estado,
            'rol': self.rol,
            'nombre_usuario': self.nombre_usuario,
            'contrasegna': self.contrasegna,
            'altura': self.altura,
            'peso': self.peso,
            'idProfesor': self.idProfesor,
            'profesor_dni': self.profesor_dni,
            'especialidad': self.especialidad,
            'salario': self.salario
        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        dni = usuario_json.get('dni')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        fecha_nacimiento = datetime.strptime(usuario_json.get('fecha_nacimiento'), '%d-%m-%Y')
        estado = usuario_json.get('estado')
        rol = usuario_json.get('rol')
        nombre_usuario = usuario_json.get('nombre_usuario')
        contrasegna = usuario_json.get('contrasegna')

        if contrasegna:  # Si la contraseña está presente en el JSON
            contrasegna_hasheada = generate_password_hash(contrasegna)  # Hashea la contraseña
        else:
            contrasegna_hasheada = None  # Si no hay contraseña en el JSON, deja el valor como None

        return Usuario(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            estado=estado,
            rol=rol,
            nombre_usuario=nombre_usuario,
            contrasegna=contrasegna_hasheada  # Establece la contraseña hasheada en el objeto Usuario
        )



# @event.listens_for(Usuario, 'before_update')
# def prevent_rol_change(mapper, connection, target):
#     if target.rol != db.session.dirty.get.rol:
#         raise Exception('No se puede cambiar el rol de un usuario.')
