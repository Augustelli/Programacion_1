from main import db


class Planificaciones_Usuario(db.Model):

    __tablename__ = 'planificaciones_usuario'
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'))
    idPlanificacion = db.Column(db.Integer, db.ForeignKey('planificacion.idPlanificacion'))

    def __repr__(self):
        return f'<Planificaciones_Usuario - idUsuario:{self.idUsuario} - idPlanificacion: {self.idPlanificacion}>'

    def to_json(self):
        planificaciones_usuarios_json = {
            'idUsuario': self.idUsuario,
            'idPlanificacion': self.idPlanificacion
        }
        return planificaciones_usuarios_json

    @staticmethod
    def from_json(planificaciones_usuarios_json):
        idUsuario = planificaciones_usuarios_json.get('idUsuario')
        idPlanificacion = planificaciones_usuarios_json.get('idPlanificacion')
        return Planificaciones_Usuario(
            idUsuario=idUsuario,
            idPlanificacion=idPlanificacion
        )
