from .. import db
from datetime import datetime
from sqlalchemy import func


class PlanificacionDetalle(db.Model):
    __tablename__ = 'planificacion_detalle'

    idPlanificacionDetalle = db.Column(db.Integer, primary_key=True)
    idPlanificacion = db.Column(db.Integer, db.ForeignKey('planificacion.idPlanificacion'))
    nombre = db.Column(db.String(50), nullable=False)
    repeticion = db.Column(db.Integer, nullable=False)
    rir = db.Column(db.Integer, nullable=False)



    def __repr__(self):
            return f'<Planificacion detalle: {self.idPlanificacion}- nombre:{self.nombre} - repeticion: {self.repeticion} - rir: {self.rir}>'

        

    def to_json(self):
        planificacion_detalle_json = {
            'idPlanificacionDetalle': self.idPlanificacionDetalle,
            'idPlanificacion': self.idPlanificacion,
            'nombre': self.nombre,
            'repeticion': self.repeticion,
            'rir': self.rir,
            
        }
        return planificacion_detalle_json

    @staticmethod
    def from_json(planificacion_detalle_json):
        idPlanificacionDetalle = planificacion_detalle_json.get('idPlanificacionDetalle')
        idPlanificacion = planificacion_detalle_json.get('idPlanificacion')
        nombre = planificacion_detalle_json.get('nombre')
        repeticion = planificacion_detalle_json.get('repeticion')
        rir = planificacion_detalle_json.get('rir')
        
        return PlanificacionDetalle(
            idPlanificacionDetalle=idPlanificacionDetalle,
            idPlanificacion=idPlanificacion,
            nombre=nombre,
            repeticion=repeticion,
            rir=rir,
            
        )
