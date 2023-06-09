from .. import db
from sqlalchemy import Float
from datetime import datetime
# from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash


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
    fecha_nacimiento = db.Column(db.DateTime, nullable=True)
    estado = db.Column(db.Boolean, default=False)
    rol = db.Column(db.String(10), default="alumno")
    nombre_usuario = db.Column(db.String(12), default=same_as('dni'))
    contrasegna = db.Column(db.String(128), nullable=False)
    altura = db.Column(Float, nullable=True)
    peso = db.Column(Float, nullable=True)
    
    # Definimos la relación uno a uno con la tabla Alumno
    alumno = db.relationship('Alumno', back_populates='usuario', uselist=False)
    profesor = db.relationship('Profesor', back_populates='usuario', uselist=False)
    usuario_pagos = db.relationship('Pagos', back_populates='pagos_usuario', cascade='all, delete-orphan', single_parent=True)
    login1 = db.relationship('Login_usuario', back_populates='usuario', uselist=False)

# class Usuario(db.Model):
#     __tablename__ = 'usuario'

#     dni = db.Column(db.Integer, primary_key=True, autoincrement=False)
#     nombre = db.Column(db.String(50), nullable=False, default=lambda: str(Usuario.dni))
#     apellido = db.Column(db.String(50), nullable=False, default=lambda: str(Usuario.dni))
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     fecha_nacimiento = db.Column(db.Date, nullable=True)
#     estado = db.Column(db.Boolean, nullable=False, default=False)
#     # Recordar que para crear la contraseña necesitamos llamar al método crear_contraseña para que compute el hash y lo almacene
#     rol = db.Column(db.String(10), nullable=False)
#     nombre_usuario = db.Column(db.String(50), db.ForeignKey('usuario_contrasegna.nombre_usuario'))
#     altura = db.Column(Float, nullable=True)
#     peso = db.Column(Float, nullable=True)

#     #   ** RELACIONES de Usuario
#     usuario_alumno = db.relationship('Alumno', uselist=False, back_populates='alumno_usuario', single_parent=True)
#     usuario_profesor = db.relationship('Profesor', uselist=False, back_populates='profesor_usuario',  single_parent=True)
#     usuario_usuario_contrasegna = db.relationship('Usuario_Contrasegna', uselist=False, back_populates='usuario_contrasegna_usuario')
#     usuario_pagos = db.relationship('Pagos', uselist=False, back_populates='pagos_usuario')
#     # Valor por defecto alumno
    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')

    @plain_password.setter
    def plain_password(self, password):
        self.contrasegna = generate_password_hash(password)

    def validate_pass(self, password):
        return check_password_hash(self.contrasegna, password)

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)
        if self.rol is None:
            self.rol = 'alumno'

    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    #Setter de la contraseña toma un valor en texto plano
    # calcula el hash y lo guarda en el atributo password
    @plain_password.setter
    def plain_password(self, password):
        self.contrasegna = generate_password_hash(password)
    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,password):
        return check_password_hash(self.contrasegna, password)       

    def __repr__(self):
        return f'<Usuario: {self.nombre} {self.apellido} {self.estado}>'

    # @validates('rol')
    # def validate_rol(self,key,rol):

    #     if self.rol != rol:
    #         raise ValueError(f'El rol del usuario debe ser {rol}')
    #     return rol

    def to_json(self):

        usuario_json = {
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'fecha_nacimiento': str(self.fecha_nacimiento.strftime("%d-%m-%Y")),
            'estado': self.estado,
            'rol': self.rol,
            'nombre_usuario': self.nombre_usuario,
            #'contrasegna': self.contrasegna,
            'altura': self.altura,
            'peso': self.peso
        }
        return usuario_json

    # def to_json_complete(self):
    #     usuario_json = {
    #         'dni': self.dni,
    #         'nombre': self.nombre,
    #         'apellido': self.apellido,
    #         'email': self.email,
    #         'fecha_nacimiento': str(self.fecha_nacimiento.strftime("%d-%m-%Y")),
    #         'estado': self.estado,
    #         'rol': self.rol,
    #         'nombre_usuario': self.nombre_usuario,
    #         'contrasegna': self.contrasegna,
    #         'altura': self.altura,
    #         'peso': self.peso,
    #         'idProfesor': self.idProfesor,
    #         'profesor_dni': self.profesor_dni,
    #         'especialidad': self.especialidad,
    #         'salario': self.salario
    #     }
    #     return usuario_json

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
        #contrasegna = usuario_json.get('contrasegna')
        altura = usuario_json.get('altura')
        peso = usuario_json.get('peso')

        return Usuario(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            estado=estado,
            rol=rol,
            nombre_usuario=nombre_usuario,
            plain_password=contrasegna,
            altura=altura,
            peso=peso,
        )

# @event.listens_for(Usuario, 'before_update')
# def prevent_rol_change(mapper, connection, target):
#     if target.rol != db.session.dirty.get.rol:
#         raise Exception('No se puede cambiar el rol de un usuario.')
