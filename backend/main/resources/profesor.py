from flask_restful import Resource
from flask import request, abort
import json



# class ProfesoresClases(Resource):

#     def get(self):
#         return clases
    

class ProfesorClases(Resource):
    def get(self, user_id ):
        if int(user_id) in clases:
            return clases[user_id]
        else:
            return '', 404 
clases = {
    "1":"Lunes, miercoles, viernes",
    "2" : "Martes, Jueves,",
    "3" : "Lunes, Martes, Miercoles",
    "4": "Jueves, Viernes"  
}