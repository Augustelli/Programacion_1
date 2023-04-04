from flask_restful import Resource
from flask import request, abort
import json

with open('json_ex.json') as JSON:
    data = json.load(JSON)


class PlanificacionAlumno(Resource):

    pass

class PlanificacionAlumnos(Resource):
    pass

class PlanificacionProfesor(Resource):
    pass


class PlanificacionProfesores(Resource):
    pass


class ProfesorClases(Resource):
    pass

class Pago(Resource):
    pass

class Login(Resource):
    pass