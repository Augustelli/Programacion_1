from flask_restful import Resource


# class ProfesoresClases(Resource):

#     def get(self):
#         return clases

class ProfesorClases(Resource):
    def get(self, user_id):
        if str(user_id) in clases:
            return clases[str(user_id)]
        else:
            return 'Éxito', 404


clases = {
    "1": "Lunes, miercoles, viernes",
    "2": "Martes, Jueves,",
    "3": "Lunes, Martes, Miercoles",
    "4": "Jueves, Viernes"
}
