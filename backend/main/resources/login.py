from flask_restful import Resource
from flask import request, abort


class Login(Resource):

    def post(self):
        try:
            informacion = request.get_json()
            id = str(int(max(db.keys())) + 1)
            db[id] = informacion
            return db[id], 201

        except BaseException:
            abort(404, 'Error al crear el log in')
    # def sing_up(self, password, user_name):
    #     pass

    # def get(self):
    #    pass


db = {
    "1": "admin",
    "2": "admin"
}
