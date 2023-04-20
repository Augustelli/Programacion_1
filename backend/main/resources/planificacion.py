from flask_restful import Resource
from flask import request, abort


class PlanificacionAlumno(Resource):

    def get(self, user_id):
        try:
            if planificaciones[user_id]:
                return planificaciones[(user_id)]
        except BaseException:
            abort(404, f'planificaciones del usuario {user_id} no encontradas')


class PlanificacionProfesor(Resource):

    def get(self, user_id):
        try:
            if planificaciones[user_id]:
                return planificaciones[user_id]
        except BaseException:
            abort(404, f'planificaciones del profe {user_id} no encontradas')

    def delete(self, user_id):
        try:
            if planificaciones[user_id]:
                del planificaciones[user_id]
                return 'Se ha eliminado con éxito', 201
        except BaseException:
            abort(404, 'No se ha encontrado la planificación del alumno.')

    def put(self, user_id):

        try:
            if planificaciones[str(user_id)]:
                data = request.get_json()
                planificaciones[str(user_id)].update(data)
                return 'Se ha editado con éxito', 201
        except BaseException:
            abort(422, 'No se ha podido realizar el cambio.')

        # try:
        #     data[user_id]['estado'] = 'deudor' if data[user_id]['estado'] == 'activo' else  'activo'  # noqa: E501
        # except:
        #     abort(422, f'No se ha podido realizar el cambio de estado.')


class PlanificacionesProfesores(Resource):

    def get(self):
        return planificaciones

    def post(self):
        try:
            informacion = request.get_json()
            id = str(int(max(planificaciones.keys())) + 1)
            planificaciones[id] = informacion
            return planificaciones[id], 201

        except BaseException:
            abort(404, 'Error al crear el usuario')


planificaciones = {
  "1": {"nombre": "Planificación 1", "descripcion": "Descripción 1", "alumno": "1", "profesor": "3", "estado": "Activa"},
  "2": {"nombre": "Planificación 2", "descripcion": "Descripción 2", "profesor": "3", "estado": "Activa"},
  "3": {"nombre": "Planificación 3", "descripcion": "Descripción 3", "alumno": "1", "estado": "Inactiva"}
}

data = {
  "0": {
    "nombre": "test",
    "apellido": "test",
    "edad": 20,
    "email": "test",
    "telefono": "+549110000000000",
    "estado": "activo",
    "rol": "admin"
  },
  "1": {
      "nombre": "Juan",
      "apellido": "Pérez",
      "edad": 25,
      "email": "juan.perez@gmail.com",
      "telefono": "+5491155555555",
      "estado": "activo",
      "rol": "prof"
    },
  "2": {
      "nombre": "María",
      "apellido": "González",
      "edad": 30,
      "email": "maria.gonzalez@hotmail.com",
      "telefono": "+5491166666666",
      "estado": "activo",
      "rol": "alumno"
    },
  "3": {
      "nombre": "Pedro",
      "apellido": "Rodríguez",
      "edad": 40,
      "email": "pedro.rodriguez@yahoo.com.ar",
      "telefono": "+5491177777777",
      "estado": "activo",
      "rol": "alumno"
    },
  "4": {
      "nombre": "Lucía",
      "apellido": "Sánchez",
      "edad": 28,
      "email": "lucia.sanchez@gmail.com",
      "telefono": "+5491188888888",
      "estado": "activo",
      "rol": "alumno"
    },
  "5": {
      "nombre": "Alejandro",
      "apellido": "Martínez",
      "edad": 35,
      "email": "alejandro.martinez@hotmail.com",
      "telefono": "+5491199999999",
      "estado": "activo",
      "rol": "alumno"
    },
  "6": {
      "nombre": "Carolina",
      "apellido": "Gómez",
      "edad": 32,
      "email": "carolina.gomez@yahoo.com.ar",
      "telefono": "+5491167676767",
      "estado": "activo",
      "rol": "alumno"
    },
  "7": {
      "nombre": "Santiago",
      "apellido": "García",
      "edad": 29,
      "email": "santiago.garcia@gmail.com",
      "telefono": "+5491156565656",
      "estado": "activo",
      "rol": "alumno"
    },
  "8": {
      "nombre": "Valentina",
      "apellido": "López",
      "edad": 27,
      "email": "valentina.lopez@hotmail.com",
      "telefono": "+5491145454545",
      "estado": "activo",
      "rol": "alumno"
    },
  "9": {
      "nombre": "Joaquín",
      "apellido": "Fernández",
      "edad": 33,
      "email": "joaquin.fernandez@yahoo.com.ar",
      "telefono": "+5491174747474",
      "estado": "activo",
      "rol": "alumno"
    },
  "10": {
      "nombre": "Ana",
      "apellido": "Pereira",
      "edad": 26,
      "email": "ana.pereira@gmail.com",
      "telefono": "+5491136363636",
      "estado": "activo",
      "rol": "alumno"
    },
  "11": {
      "nombre": "Matías",
      "apellido": "Rojas",
      "edad": 31,
      "email": "matias.rojas@hotmail.com",
      "telefono": "+5491162626262",
      "estado": "activo",
      "rol": "alumno"
    },
  "12": {
      "nombre": "Florencia",
      "apellido": "Sosa",
      "edad": 29,
      "email": "florencia.sosa@yahoo.com.ar",
      "telefono": "+5491157575757",
      "estado": "activo",
      "rol": "alumno"
    },
  "13": {
      "nombre": "Lucas",
      "apellido": "Silva",
      "edad": 34,
      "email": "lucas.silva@gmail.com",
      "telefono": "+5491168686868",
      "estado": "activo",
      "rol": "prof"
    },
  "14": {
      "nombre": "Brenda",
      "apellido": "Giménez",
      "edad": 28,
      "email": "brenda_gamer@gmail.com",
      "telefono": "+549116868685",
      "estado": "activo",
      "rol": "alumno"
    }
}
