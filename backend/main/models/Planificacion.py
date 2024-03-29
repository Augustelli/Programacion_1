from .. import db
from datetime import datetime
from sqlalchemy import func


class Planificacion(db.Model):

    __tablename__ = 'planificacion'

    idPlanificacion = db.Column(db.Integer, primary_key=True)
    rutina = db.Column(db.String(50), nullable=False)
    frecuencia = db.Column(db.String)
    fecha = db.Column(db.Date)  
    id_Alumno = db.Column(db.Integer, db.ForeignKey('alumno.idAlumno'))
    id_Clase = db.Column(db.Integer, db.ForeignKey('clases.idClases'))
    idProfesor = db.Column(db.Integer, db.ForeignKey('profesor.idProfesor'))


    alumno = db.relationship('Alumno', back_populates='planificaciones', single_parent=True)
    profesor = db.relationship('Profesor', back_populates='planificaciones', single_parent=True)
    clase = db.relationship('Clases', back_populates='planificaciones', single_parent=True)

    def __repr__(self):
        return f'<Planificaicion - idPlanificacion: {self.idPlanificacion}  - frecuencia: {self.frecuencia} - id_Clase: {self.id_Clase}>'  # noqa: E501

    def to_json(self):
        planificacion_json = {
            'idPlanificacion': self.idPlanificacion,
            'rutina': self.rutina,
            'fecha': str(self.fecha.strftime("%d-%m-%Y")),
            'frecuencia': self.frecuencia,
            'id_Alumno': self.id_Alumno,
            'id_Clase': self.id_Clase,
            'idProfesor': self.idProfesor
        }
        return planificacion_json

    @staticmethod
    def from_json(planificacion_json):
        idPlanificacion = planificacion_json.get('idPlanificacion')
        rutina = planificacion_json.get('rutina')
        fecha = datetime.strptime(planificacion_json.get('fecha'), '%d-%m-%Y')
        frecuencia = planificacion_json.get('frecuencia')
        id_Alumno = planificacion_json.get('id_Alumno')
        id_Clase = planificacion_json.get('id_Clase')
        idProfesor = planificacion_json.get('idProfesor')

        return Planificacion(
            idPlanificacion=idPlanificacion,
            rutina=rutina,
            fecha=fecha,
            frecuencia=frecuencia,
            id_Alumno=id_Alumno,
            id_Clase=id_Clase,
            idProfesor=idProfesor

        )

