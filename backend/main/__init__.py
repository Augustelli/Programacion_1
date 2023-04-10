import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources


api = Api()
# Inicialización de la App
def create_app():
    app = Flask(__name__)

    # variables de entono
    load_dotenv()

    api.add_resource(resources.UsuariosRec, '/usuarios')

    api.add_resource(resources.UsuarioRec, '/usuario/<user_id>')
   

    api.add_resource(resources.UsrsAlumnosRec, '/alumnos')

    api.add_resource(resources.UsrAlumnoRec, '/alumno/<user_id>')
   
    api.add_resource(resources.UsrProfesorRec, '/profesor/<user_id>')
   
    api.add_resource(resources.PlanAlumnoRec, '/planificacion/<user_id>')

    api.add_resource(resources.PlanProfesorRec, '/planificacion_profesor/<user_id>')


    api.add_resource(resources.PlansProfesoresRec, '/planificaciones_profesores')
    
    api.add_resource(resources.ProfesorClasesRec, '/profesor_clases/<user_id>')

    api.add_resource(resources.PagoRec, '/pago/<user_id>')

    api.add_resource(resources.LoginRec, '/login')
    api.init_app(app)
    return app