from main import db
from sqlalchemy import Float


class Profesor(db.Model):

    __tablename__ = 'profesor'

    idProfesor = db.Column(db.Integer, nullable=False, primary_key=True, index=True)
    especialidad = db.Column(db.String(50), default='No posee.')
    idClases = db.Column(db.Integer, db.ForeignKey('clases.idClases'), nuallable=False)
    # idPlanificaciones = db.Column(db.Integer, db.ForeignKey('planificaciones_profesor.id')) No se si va porque hay tabla intersección
    salario = db.Column(Float, nullable=False)

    def __repr__(self):
        profesor_json = {
            'idProfesor': self.idProfesor,
            'especialidad': self.especialidad,
            'idClases': self.idClases,
            'salario': self.salario
        }
        return profesor_json

    @staticmethod
    def from_json(profesor_json):
        idProfesor = profesor_json.get('idProfesor'),
        especialidad = profesor_json.get('especialidad')
        idClases = profesor_json.get('idClases')
        salario = profesor_json.get('salario')

        return Profesor(
            idProfesor=idProfesor,
            especialidad=especialidad,
            idClases=idClases,
            salario=salario
        )
#   ** RELACIONES de Profesor
