from .. import db


class ClaseProfesor(db.Model):
    __tablename__ = 'clases_profesor'
    idProfesor = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    idClases = db.Column(db.Integer, nullable=False)

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
