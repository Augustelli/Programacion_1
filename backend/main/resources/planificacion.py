from flask_restful import Resource
from flask import request, abort
import json
import datetime

with open('main/resource/json_planificaciones.json') as JSON:
    #Convierto JSON  a diccionario
    planificaciones = json.load(JSON)


with open('json_ex.json') as JSON:
    data = json.load(JSON)


class PlanificacionAlumno(Resource):

    def obtener_planificacion_alumno(self, user_id):
        try:
            if planificaciones[user_id]:
                return planificaciones[(user_id)]
        except:
            abort(404, f'planificaciones del usuario {user_id} no encontradas')



class PlanificacionProfesor(Resource):
    
    def obtener_planificacion(self, user_id):
        try:
            if planificaciones[user_id]:
                return planificaciones[user_id]
        except:
            abort(422, '')


    def eliminar_planificacion(self, user_id):
        try:
            if planificaciones[user_id]:
                del planificaciones[user_id]
        except:
            abort(404, 'No se ha encontrado la planificación del alumno.')

    def editar_planificaion_alumno(self, user_id, data):

        try:
            pass
        except:
            pass
    
    def cambiar_estado_alumno(self, user_id):

        try:
            data[user_id]['estado'] = 'deudor' if data[user_id]['estado'] == 'activo' else  'activo'
        except:
            abort(422, f'No se ha podido realizar el cambio de estado.')
            
class PlanificacionProfesores(Resource):
    
    def obtener_planificaciones(self):
        return planificaciones.json

    def crear_planificacion(self, user_id, data):
        try:
            if data[user_id] and planificaciones[user_id]:
                planificaciones[user_id].update(data)  #El alumno ya tiene planificaciones
            
            elif user_id in data.keys(): #alumno no tiene planificaciones previas
                planificaciones[user_id] = data
        except:
            abort(404, 'No se ha podido concretar')

