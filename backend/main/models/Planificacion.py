from .. import db


class Planificacion(db.Model):

    __tablename__ = 'planificacion'

    idPlanificacion = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    rutina = db.Column(db.String(50), nullable=False)
    frecuencia = db.Column(db.String)
    id_Alumno = db.Column(db.Integer, db.ForeignKey('alumno.idAlumno'))
    id_Clase = db.Column(db.Integer, db.ForeignKey('clases.idClases'))
    idProfesor = db.Column(db.Integer, db.ForeignKey('profesor.idProfesor'))
# RELACIONES de Planificacion

    planificacion_alumno = db.relationship('Alumno', uselist=False)
    planificaciones_profesor = db.relationship('Profesor', cascade="all, delete-orphan")
    planificacion_clases = db.relationship('Clases', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Planificaicion - idPlanificacion: {self.idPlanificacion} - planificacion: {self.planificacion} - frecuencia: {self.frecuencia} - idUsuario: {self.idUsuario} - id_Clase: {self.id_Clase}>'  # noqa: E501

    def to_json(self):
        planificacion_json = {
            'idPlanificacion': self.idPlanificacion,
            'rutina': self.rutina,
            'frecuencia': self.frecuencia,
            'id_Alumno': self.id_Alumno,
            'id_Clase': self.id_Clase
        }
        return planificacion_json

    @staticmethod
    def from_json(planificacion_json):
        idPlanificacion = planificacion_json.get('idPlanificacion')
        rutina = planificacion_json.get('rutina')
        frecuencia = planificacion_json.get('frecuencia')
        idUsuario = planificacion_json.get('idUsuario')
        id_Clase = planificacion_json.get('id_Clase')

        return Planificacion(
            idPlanificacion=idPlanificacion,
            rutina=rutina,
            frecuencia=frecuencia,
            idUsuario=idUsuario,
            id_Clase=id_Clase
        )
#   ** RELACIONES de Planificacion
