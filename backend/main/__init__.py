from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail


api = Api()
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mailsender = Mail()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ya no se necesita el archivo .db. Sino se usará el contenedor.
    # En caso de querer volver a usar el archivo .db, descomentar las siguientes líneas y crear las variables de entorno correspondientes en el archivo .env:
    # if not os.path.exists(str(os.getenv('DATABASE_PATH'))+str(os.getenv('DATABASE_NAME'))):
    #   os.mknod(str(os.getenv('DATABASE_PATH'))+str(os.getenv('DATABASE_NAME')))

    db.init_app(app)
    migrate.init_app(app, db)
    import main.resources as resources

    # Añadir recursos a endpoints
    api.add_resource(resources.UsuariosRec, '/usuarios')
    api.add_resource(resources.Clase_ProfesorRec, '/clase_profesor')
    api.add_resource(resources.UsuarioRec, '/usuario')
    api.add_resource(resources.UsrsAlumnosRec, '/alumnos')
    api.add_resource(resources.UsrAlumnoRec, '/alumno')
    api.add_resource(resources.UsrProfesorRec, '/profesor')
    # api.add_resource(resources.UsrProfesoresRec, '/profesores')
    api.add_resource(resources.PlanAlumnoRec, '/planificacion')
    api.add_resource(resources.PlanProfesorRec, '/planificacion_profesor')
    api.add_resource(resources.PlansProfesoresRec, '/planificaciones_profesores')
    api.add_resource(resources.ProfesorClasesRec, '/profesor_clases')
    api.add_resource(resources.PagoRec, '/pago')
    api.add_resource(resources.PagosRec, '/pagos')
    api.add_resource(resources.LoginRec, '/login')
    api.add_resource(resources.ClasesRec, '/clases')
    api.add_resource(resources.ClaseRec, '/clase')

    api.init_app(app)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    from main.auth import routes
    app.register_blueprint(routes.auth)

    # Configuración de mail
    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')
    # Inicializar en app
    mailsender.init_app(app)

    return app
