from flask_restful import Resource
from flask import request, abort
import json

with open('main/resource/json_planificaciones.json') as JSON:
    pagos = json.load(JSON)

with open('./json_ex.json') as JSON:
    data = json.load(JSON)
    
class Pago(Resource):
    
    def obtener_pagos_alumno(self, user_id):
        try:
            return pagos[user_id]
        except:
            abort(404, 'No se ha encontrado pagos del alumnmo')


    def actualizar_estado_alumno(self, user_id):

        try:
            data[user_id]['estado'] = 'deudor' if data[user_id]['estado'] == 'activo' else  'activo'
        except:
            abort(404, f'No se ha podido realizar el cambio de estado.')