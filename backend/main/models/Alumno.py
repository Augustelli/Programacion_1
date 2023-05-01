from .. import db


class Alumno(db.Model):

    __tablename__ = 'alumno'

    idAlumno = db.Column(db.Integer, primary_key=True)
    alumno_dni = db.Column(db.Integer, db.ForeignKey('usuario.dni'))
<<<<<<< HEAD
    usuario = db.relationship('Usuario', uselist=False, back_populates='alumno')
    planificacion = db.relationship('Planificacion', back_populates='alumno')
=======
    usuario = db.relationship('Usuario', uselist=False, back_populates='alumno', cascade='all, delete-orphan')
    planificacion = db.relationship('Planificacion', back_populates='alumno', cascade='all, delete-orphan', single_parent=True)
# RELACIONES ALumnos

    alumno_usuario = db.relationship('Usuario', back_populates='usuario_alumno')
    alumno_planificacion = db.relationship('Planificacion', back_populates='planificacion_alumno', cascade='all, delete-orphan')
>>>>>>> 887990db93a2a1af80deefb7ea9cf908b77f4940

    def __repr__(self):
        return f'<Alumno - ID:{self.idAlumno} - alumno_dni: {self.alumno_dni} >'

    def to_json(self):
        alumno_json = {
            'idAlumno': self.idAlumno,
            'alumno_dni': self.alumno_dni
        }
        return alumno_json

    @staticmethod
    def from_json(alumno_json):
        idALumno = alumno_json.get('idAlumno')
        alumno_dni = alumno_json.get('alumno_dni')
        return Alumno(
            idALumno=idALumno,
            alumno_dni=alumno_dni
        )

#   ** RELACIONES de Alumno
