from .. import db


clase_profesor = db.Table(
    'clase_profesor',
    db.Column('profesor_id', db.Integer, db.ForeignKey('profesor.idProfesor')),
    db.Column('clase_id', db.Integer, db.ForeignKey('clases.idClases'))
)



class Clases(db.Model):
    __tablename__ = 'clases'

    idClases = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    nombre = db.Column(db.String(50), nullable=False, default='Rutina personal.')
  
    dias = db.Column(db.String(50), nullable=False, default='Lunes-Miercoles-Viernes')

    profesores = db.relationship('Profesor', secondary=clase_profesor,backref='clases' )
    planificaciones = db.relationship('Planificacion', back_populates='clase', cascade='all', single_parent=True)
    
    def __repr__(self):
        return f'<Clases idClases: {self.idClases}> - Nombre: {self.nombre} -  Dias: {self.dias}'

    def to_json(self):
        return {
            'idClases': self.idClases,
            'nombre': self.nombre,
            'dias': self.dias
        }

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
