from .. import db
import hashlib


class Usuario_Contrasegna(db.Model):

    __tablename__ = 'usuario_contrasegna'
    nombre_usuario = db.Column(db.String, primary_key=True)
    contrasegna_hash = db.Column(db.String(64), nullable=False)
# RELACIONES Usuario_Contrasegna
    usuario_contrasegna_usuario = db.relationship('Usuario', back_populates='usuario_usuario_contrasegna', uselist=False, cascade='all, delete-orphan')
    usuario_contrasegna_login = db.relationship('Loging_Usuario', back_populates='login_usuario_contrasegna', cascade='all, delete-orphan', single_parent=True)

    def __repr__(self):
        return f'<Usuario Contrasegna - nombre_usuario:{self.nombre_usuario} - contrasegna_hash: {self.contrasegna_hash}>'

    def to_json(self):
        usuario_contrasegna = {
            'nombre_usuario': self.nombre_usuario,
            'contrasegna_hash': self.contrasegna_hash
        }
        return usuario_contrasegna

    def crear_contrasegna(self, contrasegna):
        self.password_hash = hashlib.sha256(contrasegna.encode('utf-8')).hexdigest()

    def checkear_contrasegna(self, contrasegna):
        return self.password_hash == hashlib.sha256(contrasegna.encode('utf-8')).hexdigest()

    @staticmethod
    def from_json(usuario_contrasegna):
        nombre_usuario = usuario_contrasegna.get('nombre_usuario')
        contrasegna_hash = usuario_contrasegna.get('contrasegna_hash')
        return Usuario_Contrasegna(
            nombre_usuario=nombre_usuario,
            contrasegna_hash=contrasegna_hash
        )
