from .. import db
from sqlalchemy import DateTime
from datetime import datetime


class Login_usuario(db.Model):

    __tablename__ = 'login_usuario'
    id_nombre_usuario = db.Column(db.Integer, primary_key=True, index=True)
    nombre_usuario = db.Column(db.String(50), db.ForeignKey('usuario.nombre_usuario'))
    contrasegna=db.Column(db.String(50))
    fecha_login = db.Column(DateTime, nullable=False, default=datetime.now())
    # RELACIONES de login_usuario
    #login_usuario_contrasegna = db.relationship('Usuario_Contrasegna', back_populates='usuario_contrasegna-login', cascade='all, delete-orphan', single_parent=True)
    #login_usuario_contrasegna = db.relationship('Usuario_contrasegna', back_populates='login', uselist=False)
    usuario=db.relationship('Usuario', back_populates='login1', cascade='all, delete-orphan', single_parent=True)


    def __repr__(self):
        return f'<Login_usuario - nombre_usuario: {self.nombre_usuario} - fecha_login: {self.fecha_login}>'

    def to_json(self):
        login_usuario_json = {
            'nombre_usuario': self.nombre_usuario,
            'fecha_login': self.fecha_login
        }
        return login_usuario_json

    @staticmethod
    def from_json(login_usuario_json):
        nombre_usuario = login_usuario_json.get('nombre_usuario')
        fecha_login = login_usuario_json.get('fecha_login')

        return Login_usuario(
            nombre_usuario=nombre_usuario,
            fecha_login=fecha_login
        )
