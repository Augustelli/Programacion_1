from main import db
from datetime import datetime


class Pagos(db.Models):
    __tablename__ = 'pagos'

    idPago = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'), nullable=False)
    estado = db.Column(db.String(10), nullable=False, default='No pagado')
    fecha_pago = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Pagos idPago:{self.idPago} - idUsuario: {self.idUsuario} - estado: {self.estado} - fecha_pago: {self.fecha_pago}>'

    def to_json(self):
        pago_json = {
            'idPago': self.idPago,
            'idUsuario': self.idUsuario,
            'estado': self.estado,
            'fecha_pago': self.fecha_pago
        }
        return pago_json

    @staticmethod
    def from_json(pago_json):
        idPago = pago_json.get('idPago')
        idUsuario = pago_json.get('idUsuario')
        estado = pago_json.get('estado')
        fecha_pago = pago_json.get('fecha_pago')
        return Pagos(
            idPago=idPago,
            idUsuario=idUsuario,
            estado=estado,
            fecha_pago=fecha_pago
        )
# RELACIONES Pagos
