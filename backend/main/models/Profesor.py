from .. import db
from sqlalchemy import Float


class Profesor(db.Model):

    __tablename__ = 'profesor'

    idProfesor = db.Column(db.Integer ,nullable=False, primary_key=True, index=True)
    profesor_dni= db.Column(db.Integer, db.ForeignKey('usuario.dni'), nullable=False)
    especialidad = db.Column(db.String(50), default='No posee.')
    salario = db.Column(Float, nullable=False)
    usuario = db.relationship('Usuario', uselist=False, back_populates='profesor', cascade='all, delete-orphan')
    clases_profesor = db.relationship('ClaseProfesor', back_populates='profesor', cascade='all, delete-orphan', single_parent=True)
    

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
