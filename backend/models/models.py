from ..main import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float
from datetime import datetime, time
import hashlib


class Usuario(db.Model):
    __tablename__ = 'usuario'

    idUsuario = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    nombre = db.Column(db.String(50), nullable=False, default=lambda: str(self.idUsuario))
    apellido = db.Column(db.String(50), nullable=False, default='apellido')
    fecha_nacimiento = db.Column(db.Date, nullable=False, default=datetime.date.today())
    email = db.Column(db.String(50), nullable=False, unique=True)
    # Recordar que para crear la contraseña necesitamos llamar al método crear_contraseña para que compute el hash y lo almacene
    password_hash = db.Column(db.String(64), nullable=False)
    rol = db.Column(db.String(10), nullable=False)
    altura = db.Column(Float, nullable=True)
    peso = db.Column(Float, nullable=True)
    dni = db.Column(db.Integer(8), nullable=False, unique=True)

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

#   ** RELACIONES de Usuario


class Profesor(db.Model):

    __tablename__ = 'profesor'

    idProfesor = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    especialidad = db.Column(db.String(50), default='No posee.')
    idClases = db.Column(db.Integer, db.ForeignKey('clases.idClases'), nuallable=False)
    # idPlanificaciones = db.Column(db.Integer, db.ForeignKey('planificaciones_profesor.id')) No se si va porque hay tabla intersección
    salario = db.Column(Float, nullable=False)

#   ** RELACIONES de Profesor


class Alumno(db.Model):

    __tablename__ = 'alumno'

    idAlumno = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    planificacion = db.Column(db.Integer, db.ForeignKey('planificacion_usuario.idPlanificacion'), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=False)

#   ** RELACIONES de Alumno


class ClaseProfesor(db.Model):
    __tablename__ = 'clases_profesor'
    idProfesor = db.Column(db.Integer, db.ForeignKey('profesor.idProfesor'), nullable=False)
    idClases = db.Column(db.Integer, db.ForeignKey('clases.idClases'), nullable=False)

#   ** RELACIONES de Clases_Profesor


class Clases(db.Model):
    
    __tablename__ = 'clases'

    idClases = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, default='Rutina personal.')
    horario = db.Column(db.Time, default=time(0, 0))

#   ** RELACIONES de Clases


class Planificacion(db.Model):

    __tablename__ = 'planificacion'

    idPlanificacion = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    planificacion = db.Column(db.String)  # json ???
    frecuencia = db.Column(db.String)

    idUsuario = db.Column(db.Integer, db.ForeingKey('planificiaciones_usuario.idUsuario'), nullable=False)  # Me parece que tiene que ser como el de abajo
    idUsuario = db.Column(db.Integer, db.ForeingKey('usuario.idUsuario'), nullable=False)
    idClase = db.Column(db.Integer, db.ForeingKey('clases.idClases'), nullable=False)


#   ** RELACIONES de Planificacion


class Planificaciones_Usuario(db.Model):

    __tablename__ = 'planificaciones_usuario'
    idUsuario = db.Column(db.Integer, db.ForeignKey('planificacion.idP'))


class Planificaciones_Profesor(db.Model):
    pass

# Las planificaciones las deje para cuando nos veamos

    __tablename__ = 'pagos'

    idPago = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'), nullable=False)
    estado = db.Column(db.String(10), nullable=False, default='No pagado')
    fecha_pago = db.Column(db.DateTime, default=datetime.utcnow())

#   ** RELACIONES de Pagos