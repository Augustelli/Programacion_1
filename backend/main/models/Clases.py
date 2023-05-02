from .. import db
from datetime import time

# clase_profesor = db.Table(
#     "profesores_clases",
#     db.Column("id_clase", db.Integer, db.ForeignKey("clases.idClases")),
#     db.Column("id_profesor", db.Integer, db.ForeignKey("profesor.idProfesor"))

clase_profesor = db.Table('clase_profesor',
    db.Column('profesor_id', db.Integer, db.ForeignKey('profesor.idProfesor'), primary_key=True),
    db.Column('clase_id', db.Integer, db.ForeignKey('clases.idClases'), primary_key=True)
)
class Clases(db.Model):


    __tablename__ = 'clases'

    idClases = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    nombre = db.Column(db.String(50), nullable=False, default='Rutina personal.')
    #horario = db.Column(db.Time, default=time(0, 0))
    dias = db.Column(db.String(50), nullable=False, default='Lunes-Miercoles-Viernes')

    # Relaciones Clases

    #clases_planificiacion = db.relationship('Planificacion', uselist=False)
    profesores = db.relationship('Profesor', secondary=clase_profesor, back_populates='clases')
    planificaciones = db.relationship('Planificacion', back_populates='clase',cascade='all, delete-orphan', single_parent=True)
    #clases_planificaciones = db.relationship('Planificacion', backref='clase')



    # def __repr__(self):
    #     return f'<Clases idClases: {self.idClases}> - Nombre: {self.nombre} - Horario: {self.horario} - Dias: {self.dias}'
    def __repr__(self):
        return f'<Clases idClases: {self.idClases}> - Nombre: {self.nombre} -  Dias: {self.dias}'

    def to_json(self):
        clases_json = {
            'idClases': self.idClases,
            'nombre': self.nombre,
            'dias': self.dias
        }
        return clases_json

    @staticmethod
    def from_json(clases_json):
        idClases = clases_json.get('idClases')
        nombre = clases_json.get('nombre')
        dias = clases_json.get('dias')
        return Clases(
            idClases=idClases,
            nombre=nombre,
            dias=dias
        )
