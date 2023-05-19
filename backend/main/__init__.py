from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate


api = Api()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # variables de entono
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getenv('DATABASE_PATH')}{os.getenv('DATABASE_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not os.path.exists(str(os.getenv('DATABASE_PATH'))+str(os.getenv('DATABASE_NAME'))):
        os.mknod(str(os.getenv('DATABASE_PATH'))+str(os.getenv('DATABASE_NAME')))

    db.init_app(app)
    migrate.init_app(app, db)
    import main.resources as resources
    api.add_resource(resources.UsuariosRec, '/usuarios')


    api.add_resource(resources.Clase_ProfesorRec, '/clase_profesor')

    # api.add_resource(resources.UsuarioRec, '/usuario/<user_id>')

    # api.add_resource(resources.UsrsAlumnosRec, '/alumnos')

    # api.add_resource(resources.UsrAlumnoRec, '/alumno/<user_id>')

    # api.add_resource(resources.UsrProfesorRec, '/profesor/<user_id>')
    # api.add_resource(resources.UsrProfesoresRec, '/profesores')

    api.add_resource(resources.PlanAlumnoRec, '/planificacion')

#    api.add_resource(resources.PlanProfesorRec, '/planificacion_profesor/<user_id>')

    api.add_resource(resources.PlansProfesoresRec, '/planificaciones_profesores')

    #api.add_resource(resources.ProfesorClasesRec, '/profesor_clases')

    api.add_resource(resources.PagoRec, '/pago/<user_id>')

    api.add_resource(resources.PagosRec, '/pagos')

    api.add_resource(resources.LoginRec, '/login')

    # api.add_resource(resources.ClaseRec, '/clase/<idclase>')

    api.add_resource(resources.ClasesRec, '/clases')
    #api.add_resource(resources.ClaseRec, '/clase/<user_id>')

    api.add_resource(resources.ProfesorClasesRec, '/profesor_clases')

    api.init_app(app)
    return app
