from .. import db


class Alumno(db.Model):

    __tablename__ = 'alumno'

    idAlumno = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    planificacion = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Alumno - ID:{self.idAlumno} - estado: {self.estado}\nPlanificacion: {self.planificacion} >'

    def to_json(self):
        alumno_json = {
            'idAlumno': self.idAlumno,
            'planificacion': self.planificacion,
            'estado': self.estado
        }
        return alumno_json

    @staticmethod
    def from_json(alumno_json):
        idALumno = alumno_json.get('idAlumno')
        planificacion = alumno_json.get('planificacion')
        estado = alumno_json.get('estado')
        return Alumno(
            idALumno=idALumno,
            planificacion=planificacion,
            estado=estado
        )

#   ** RELACIONES de Alumno
