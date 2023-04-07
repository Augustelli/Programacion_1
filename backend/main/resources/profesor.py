from flask_restful import Resource
from flask import request, abort
import json

with open('json_clsaes_profesor.json','w+') as JSON:
    clases = json.load(JSON)

class ProfesorClases(Resource):

    def obtener_clases_profesor(self):
        return clases