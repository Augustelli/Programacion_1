from main import db


class Planificacion(db.Model):

    __tablename__ = 'planificacion'

    idPlanificacion = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    planificacion = db.Column(db.String)
    frecuencia = db.Column(db.String)

    idUsuario = db.Column(db.Integer, db.ForeingKey('planificiaciones_usuario.idUsuario'), nullable=False)  # Me parece que tiene que ser como e abajo
    idClase = db.Column(db.Integer, db.ForeingKey('clases.idClases'), nullable=False)

    def __repr__(self):
        return f'<Planificaicion - idPlanificacion: {self.idPlanificacion} - planificacion: {self.planificacion} - frecuencia: {self.frecuencia} - idUsuario: {self.idUsuario} - idClase: {self.idClase}>'  # noqa: E501

    def to_json(self):
        planificacion_json = {
            'idPlanificacion': self.idPlanificacion,
            'planificacion': self.planificacion,
            'frecuencia': self.frecuencia,
            'idUsuario': self.idUsuario,
            'idClase': self.idClase
        }
        return planificacion_json

    @staticmethod
    def from_json(planificacion_json):
        idPlanificacion = planificacion_json.get('idPlanificacion')
        planificacion = planificacion_json.get('planificacion')
        frecuencia = planificacion_json.get('frecuencia')
        idUsuario = planificacion_json.get('idUsuario')
        idClase = planificacion_json.get('idClase')

        return Planificacion(
            idPlanificacion=idPlanificacion,
            planificacion=planificacion,
            frecuencia=frecuencia,
            idUsuario=idUsuario,
            idClase=idClase
        )
#   ** RELACIONES de Planificacion
