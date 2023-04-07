from flask_restful import Resource
from flask import request, abort
import json
import hashlib as hash

with open('main/resource/json_db.json') as JSON:
    db= json.load(JSON)
    
class Login(Resource):
    

    def login(self, user_name, password):

        try:
            if user_name in db:
                try:
                    if hash.sha256(password.encode()) == db[user_name]:
                        return 'Accedido'
                        #Luego deberá redireccionar
                except:
                    abort(422, 'Error al iniciar sesion')

        except:
            abort(404, 'No se ha encontrado ese usuario')

    def sing_up(self, password, user_name):
        
        try:
            db[user_name] = hash.sha256(password.encode())
        except:
            abort(500, f'No se ha podido realizar.')
    

    def get(self):
        return db