from .. import db


class Profesor(db.Model):

    __tablename__ = 'profesor'

    idProfesor = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    profesor_dni = db.Column(db.Integer, db.ForeignKey('usuario.dni'), nullable=False)
    especialidad = db.Column(db.String(50), default='No posee.')
    salario = db.Column(db.Float, nullable=False)
<<<<<<< HEAD
    usuario = db.relationship('Usuario', uselist=False, back_populates='profesor')
    clases_profesor = db.relationship('ClaseProfesor', back_populates='profesor')
    planificaciones = db.relationship('Planificacion', back_populates='profesor')
=======

#   ** RELACIONES de Profesor
    profesor_usuario = db.relationship('Usuario', back_populates='usuario_profesor', cascade='all, delete-orphan')
    profesor_planificaciones = db.relationship('Planificaciones', uselist=False, back_populates='planificaciones_profesor')
    profesor_clases = db.relationship('Clase', uselist=False, back_populates='clases_profesores')
>>>>>>> 887990db93a2a1af80deefb7ea9cf908b77f4940

    def __repr__(self):
        profesor_json = {
            'idProfesor': self.idProfesor,
            'profesor_dni': self.profesor_dni,
            'especialidad': self.especialidad,
            'salario': self.salario
        }
        return profesor_json

    @staticmethod
    def from_json(profesor_json):
        idProfesor = profesor_json.get('idProfesor'),
        profesor_dni = profesor_json.get('profesor_dni')
        especialidad = profesor_json.get('especialidad')
        salario = profesor_json.get('salario')

        return Profesor(
            idProfesor=idProfesor,
            profesor_dni=profesor_dni,
            especialidad=especialidad,
            salario=salario
        )
#   ** RELACIONES de Profesor
