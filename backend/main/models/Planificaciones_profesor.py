# from .. import db


# class Planificaciones_Profesor(db.Model):

#     idProfesor = db.Column(db.Integer, primary_key=True, index=True)
#     idPlanificacion = db.Column(db.Integer)

#     def __repr__(self):
#         return f'<Planificaciones_Profesor - idProfesor: {self.idProfesor} - idPlanificacion: {self.idPlanificacion}>'

#     def to_json(self):
#         planificaciones_profesor_json = {
#             'idProfesor': self.idProfesor,
#             'idPlanificacion': self.idPlanificacion
#         }
#         return planificaciones_profesor_json

#     @staticmethod
#     def from_json(planificaciones_profesor_json):
#         idProfesor = planificaciones_profesor_json.get('idProfesor')
#         idPlanificacion = planificaciones_profesor_json.get('idPlanificacion')

#         return Planificaciones_Profesor(
#             idProfesor=idProfesor,
#             idPlanificacion=idPlanificacion
#         )
# RELACIONES de planificaciones_profesor
