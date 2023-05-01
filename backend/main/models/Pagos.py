from .. import db
from datetime import datetime


class Pagos(db.Model):
    __tablename__ = 'pagos'

    idPago = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    monto = db.Column(db.Integer, nullable=False)
    fecha_de_pago = db.Column(db.DateTime, default=datetime.utcnow())
    estado = db.Column(db.String(10), nullable=False, default='No pagado')
    dni = db.Column(db.Integer, db.ForeignKey('usuario.dni'), nullable=False)

    # Relacion Pagos
    pagos_usuario = db.relationship('Usuario', back_populates='usuario_pagos')
    

    def __repr__(self):
        return f'<Pagos idPago:{self.idPago} - monto: {self.monto} - fecha_pago: {self.fecha_pago}  - estado: {self.estado} >'

    def to_json(self):
        pago_json = {
            'idPago': self.idPago,
            'monto': self.monto,
            'fecha_pago': self.fecha_pago,
            'estado': self.estado,
            'dni': self.dni
        }
        return pago_json

    @staticmethod
    def from_json(pago_json):
        idPago = pago_json.get('idPago')
        monto = pago_json.get('monto')
        fecha_pago = pago_json.get('fecha_pago')
        estado = pago_json.get('estado')
        dni = pago_json.get('dni')
        return Pagos(
            idPago=idPago,
            monto=monto,
            fecha_pago=fecha_pago,
            estado=estado,
            dni=dni
        )

