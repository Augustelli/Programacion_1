from flask_restful import Resource
from flask import request, abort
import json
import hashlib as hash


    
class Login(Resource):
    

    def post(self, user_name, password):

        try:
            nuevo_usuario = request.json()
            id = str(int(db.keys())+1)
            db[id] = nuevo_usuario
            return db[id], 201

        except:
            abort(404, 'No se ha encontrado ese usuario')

    # def sing_up(self, password, user_name):
    #     pass
    

    # def get(self):
    #    pass
    


db = {

    "admin":"admin",
    "Augusto" : "admin"
}