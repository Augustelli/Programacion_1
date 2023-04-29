from .. import db
from datetime import time


class Clases(db.Model):

    __tablename__ = 'clases'

    idClases = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    nombre = db.Column(db.String(50), nullable=False, default='Rutina personal.')
    horario = db.Column(db.Time, default=time(0, 0))
    dias = db.Column(db.String(50), nullable=False, default='Lunes-Miercoles-Viernes')

    # Relaciones Clases
    clasesProfesor = db.relationship('ClaseProfesor', back_populates='clases', cascade='all, delete-orphan')
    planificaciones = db.relationship('Planificaciones', back_populates='clases', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Clases idClases: {self.idClases}> - Nombre: {self.nombre} - Horario: {self.horario} - Dias: {self.dias}'

    def to_json(self):
        clases_json = {
            'idClases': self.idClases,
            'nombre': self.nombre,
            'horario': self.horario,
            'dias': self.dias
        }
        return clases_json

    @staticmethod
    def from_json(clases_json):
        idClases = clases_json.get('idClases')
        nombre = clases_json.get('nombre')
        horario = clases_json.get('horario')
        dias = clases_json.get('dias')
        return Clases(
            idClases=idClases,
            nombre=nombre,
            horario=horario,
            dias=dias
        )
