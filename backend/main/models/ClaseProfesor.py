from main import db


class ClaseProfesor(db.Model):
    __tablename__ = 'clases_profesor'
    idProfesor = db.Column(db.Integer, db.ForeignKey('profesor.idProfesor'), nullable=False)
    idClases = db.Column(db.Integer, db.ForeignKey('clases.idClases'), nullable=False)

#   ** RELACIONES de Clases_Profesor

    def __repr__(self):
        return f'<Clase Profesor: idProfesor: {self.idProfesor} - idClases: {self.idClases}>'

    def to_json(self):
        clase_profesor = {
            'idProfesor': self.idProfesor,
            'idClases': self.idClases
        }
        return clase_profesor

    @staticmethod
    def from_json(claseProfesor_json):
        idProfesor = claseProfesor_json.get('idProfesor')
        idClases = claseProfesor_json.get('idClases')
        return ClaseProfesor(
            idProfesor=idProfesor,
            idClases=idClases
        )
