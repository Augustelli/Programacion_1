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

    api.add_resource(resources.UsuariosRec, '/usuarios_obtener')
    api.add_resource(resources.UsuariosRec, '/usuarios_crear/<user_id>')

    api.add_resource(resources.UsuarioRec, '/usuario_obtener/<user_id>')
    api.add_resource(resources.UsuarioRec, '/usuario_editar/<user_id>/<data>')
    api.add_resource(resources.UsuarioRec, '/usuario_eliminar/<user_id>')

    api.add_resource(resources.UsrAlumnosRec, '/alumnos_obtener')
    api.add_resource(resources.UsrAlumnosRec, '/alumnos_crear/<data>')
    api.add_resource(resources.UsrAlumnoRec, '/alumno_obtener/<user_id>')
    api.add_resource(resources.UsrAlumnoRec, '/alumno_eliminar/<user_id>')
    api.add_resource(resources.UsrAlumnoRec, '/alumno_cambiar_estado/<user_id>')

    api.add_resource(resources.UsrProfesorRec, '/profesor_obtener')
    api.add_resource(resources.UsrProfesorRec, '/profesor_crear/<data>')
    api.add_resource(resources.UsrProfesorRec, '/profesor_editar_alumno/<user_id>/<data>')

    api.add_resource(resources.PlanAlumnoRec, '/planificacion_alumno_obtener/<user_id>')

    api.add_resource(resources.PlanProfesorRec, '/planificacion_profesor_obtener/<user_id>')
    api.add_resource(resources.PlanProfesorRec, '/planificacion_profesor_eliminar/<user_id>')
    api.add_resource(resources.PlanProfesorRec, '/planificacion_profesor_editar/<user_id>/<data>')
    api.add_resource(resources.PlanProfesorRec, '/planificacion_profesor_cambiar_estado/<user_id>')

    api.add_resource(resources.PlanProfesoresRec, '/planificacion_profesores_clases_obtener')
    api.add_resource(resources.PlanProfesoresRec, '/planificacion_profesores_clases_crear/<user_id>/<data>')
    
    api.add_resource(resources.ProfesorClasesRec, '/profesores_clases_obtener')

    api.add_resource(resources.PagoRec, '/pago_obtener/<user_id>')
    api.add_resource(resources.PagoRec, '/pago_actulizar_estado/<user_id>')

    
    api.add_resource(resources.LoginRec, '/login/user_name/password')
    api.add_resource(resources.LoginRec, '/sign_up/user_name/password')
    api.add_resource(resources.LoginRec, '/login_get')
    
    api.init_app(app)
    return app