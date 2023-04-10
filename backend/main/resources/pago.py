from flask_restful import Resource
from flask import request, abort
import json


class Pago(Resource):
    
    def get(self, user_id):
        try:
            if str(user_id) in pagos:
                return pagos[str(user_id)]
        except:
            abort(404, 'No se ha encontrado pagos del alumnmo')


# class Pagos(Resource):
    
#     def get(self):
#         try:
#             return pagos
#         except:
#             abort(404, 'No se ha encontrado pagos.')

pagos = {

  "1": {'alumno': '1', 'monto': '1000', 'estado': 'Pendiente'},
  "2": {'alumno': '2', 'monto': '1500', 'estado': 'Pagado'},

  }
