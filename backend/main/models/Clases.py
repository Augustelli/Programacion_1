from main import db
from datetime import time


class Clases(db.Model):

    __tablename__ = 'clases'

    idClases = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, default='Rutina personal.')
    horario = db.Column(db.Time, default=time(0, 0))

    def __repr__(self):
        return f'<Clases idClases: {self.idClases}> - Nombre: {self.nombre} - Horario: {self.horario}'

    def to_json(self):
        clases_json = {
            'idClases': self.idClases,
            'nombre': self.nombre,
            'horario': self.horario
        }
        return clases_json

    @staticmethod
    def from_json(clases_json):
        idClases = clases_json.get('idClases')
        nombre = clases_json.get('nombre')
        horario = clases_json.get('horario')
        return Clases(
            idClases=idClases,
            nombre=nombre,
            horario=horario
        )
#   ** RELACIONES de Clases
