from .. import db
from sqlalchemy import Float
from datetime import datetime
import hashlib


class Usuario(db.Model):
    __tablename__ = 'usuario'

    idUsuario = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    nombre = db.Column(db.String(50), nullable=False, default=str(idUsuario))
    apellido = db.Column(db.String(50), nullable=False, default='apellido')
    fecha_nacimiento = db.Column(db.Date, nullable=False, default=datetime.date.today())
    email = db.Column(db.String(50), nullable=False, unique=True)
    # Recordar que para crear la contraseña necesitamos llamar al método crear_contraseña para que compute el hash y lo almacene
    password_hash = db.Column(db.String(64), nullable=False)
    rol = db.Column(db.String(10), nullable=False)
    altura = db.Column(Float, nullable=True)
    peso = db.Column(Float, nullable=True)
    dni = db.Column(db.Integer(8), nullable=False, unique=True)
    estado = db.Column(db.Boolean, nullable=False, default=False)

    def crear_contrasegna(self, contrasegna):
        self.password_hash = hashlib.sha256(contrasegna.encode('utf-8')).hexdigest()

    def checkear_contrasegna(self, contrasegna):
        return self.password_hash == hashlib.sha256(contrasegna.encode('utf-8')).hexdigest()
    # Valor por defecto alumno

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)
        if self.role is None:
            self.role = 'alumno'

    def establecer_role(self, role):
        if role not in ['alumno', 'profesor', 'admin']:
            raise ValueError('Rol inválido')
        self.role = role

    def __repr__(self):
        return f'<Usuario: {self.nombre} {self.apellido} {self.estado}>'

    def to_json(self):

        usuario_json = {
            'idUsuario': self.idUsuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'fecha_nacimiento': self.fecha_nacimiento,
            'email': self.email,
            'password_hash': self.password_hash,
            'rol': self.rol,
            'altura': self.altura,
            'peso': self.peso,
            'dni': self.dni,
            'estado': self.estado
        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        idUsuario = usuario_json.get('idUsuario')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        fecha_nacimiento = usuario_json.get('fecha_nacimiento')
        email = usuario_json.get('email')
        password_hash = usuario_json.get('password_hash')
        rol = usuario_json.get('rol')
        altura = usuario_json.get('altura')
        peso = usuario_json.get('peso')
        dni = usuario_json.get('dni')
        estado = usuario_json.get('estado')

        return Usuario(
            idUsuario=idUsuario,
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            password_hash=password_hash,
            rol=rol,
            altura=altura,
            peso=peso,
            dni=dni,
            estado=estado,
        )

#   ** RELACIONES de Usuario
