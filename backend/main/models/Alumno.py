from .. import db


class Alumno(db.Model):
    __tablename__ = 'alumno'

    idAlumno = db.Column(db.Integer, primary_key=True)
    alumno_dni = db.Column(db.Integer, db.ForeignKey('usuario.dni'))
    altura = db.Column(db.Float, nullable=True)
    peso = db.Column(db.Float, nullable=True)
    usuario = db.relationship('Usuario', back_populates='alumno', uselist=False)
    # planificaciones = db.relationship('Planificacion', back_populates='alumno')
    planificaciones = db.relationship('Planificacion', back_populates='alumno', cascade='all, delete-orphan', single_parent=True)
#     __tablename__ = 'alumno'
#     idAlumno = db.Column(db.Integer, primary_key=True)
#     alumno_dni = db.Column(db.Integer, db.ForeignKey('usuario.dni'))
#    # usuario = db.relationship('Usuario', uselist=False, back_populates='alumno', cascade='all, delete-orphan')
#     planificacion = db.relationship('Planificacion', back_populates='alumno', cascade='all, delete-orphan', single_parent=True)
# # RELACIONES ALumnos

#     alumno_usuario = db.relationship('Usuario', back_populates='usuario_alumno', single_parent=True,uselist=False, cascade='all, delete-orphan')
#     alumno_planificacion = db.relationship('Planificacion', back_populates='planificacion_alumno', cascade='all, delete-orphan')
    def __repr__(self):
        return f'<Alumno - ID:{self.idAlumno} - alumno_dni: {self.alumno_dni} - peso:{self.peso} - altura:{self.altura}>'

    def to_json(self):
        alumno_json = {
            'idAlumno': str(self.idAlumno),
            'alumno_dni': str(self.alumno_dni),
            'peso': str(self.peso),
            'altura': str(self.altura)
        }
        return alumno_json

    @staticmethod
    def from_json(alumno_json):
        idALumno = alumno_json.get('idAlumno')
        alumno_dni = alumno_json.get('alumno_dni')
        peso = alumno_json.get('peso')
        altura = alumno_json.get('altura')


        return Alumno(
            idALumno=idALumno,
            alumno_dni=alumno_dni,
            peso=peso,
            altura=altura
        )

#   ** RELACIONES de Alumno
