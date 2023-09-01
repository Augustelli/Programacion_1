from .. import db


clase_profesor = db.Table(
    'clase_profesor',
    db.Column('profesor_id', db.Integer, db.ForeignKey('profesor.idProfesor')),
    db.Column('clase_id', db.Integer, db.ForeignKey('clases.idClases'))
)
<<<<<<< HEAD

    


=======
# @staticmethod
# def from_json(clases_json):
#     clase_id = clases_json.get('clase_id')
#     profesor_id = clases_json.get('profesor_id')
    
#     return clase_profesor(
#         clase_id=clase_id,
#         profesor_id=profesor_id
#     )
>>>>>>> 71ea51022825f95c495f020a406dd4ef12a4eece

# def to_json(self):
#     return {
#         'clase_id': self.clase_id,
#         'profesor_id': self.profesor_id
#     }


class Clases(db.Model):
    __tablename__ = 'clases'

    idClases = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    nombre = db.Column(db.String(50), nullable=False, default='Rutina personal.')
    # horario = db.Column(db.Time, default=time(0, 0))  # TODO :Ver como agregar horario
    dias = db.Column(db.String(50), nullable=False, default='Lunes-Miercoles-Viernes')

    # Relaciones Clases

    profesores = db.relationship('Profesor', secondary=clase_profesor,backref='clases' )
    planificaciones = db.relationship('Planificacion', back_populates='clase', cascade='all', single_parent=True)
    # def __repr__(self):
    #     return f'<Clases idClases: {self.idClases}> - Nombre: {self.nombre} - Horario: {self.horario} - Dias: {self.dias}'

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
