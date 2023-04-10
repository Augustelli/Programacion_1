from flask_restful import Resource
from flask import request, abort
import json

#Se recibe un JSON -> {key : value}
#Roles ? Valor del JSON?


class Usuarios(Resource):
    '''Colección de usurios'''

    #Como aplicar roles

    def get(self):
        '''GET -> Rol amin'''
        return datos


    def post(self):
        '''POST -> Rol admin'''
        try:
            informacion = request.get_json()
            id = str(int(max(datos.keys())) + 1)
            datos[id] = informacion
            return datos[id], 201

        except:
            abort(404, 'Error al crear el usuario')


class Usuario(Resource):
    '''Recurso de Usuario '''

    def get(self, user_id):
        '''GET -> Rik Admin'''
        try:
            if datos[str(user_id)]:
                return datos[(user_id)]
        except:
            abort(404, '')


    def put(self, user_id ):
        '''PUT -> Rol Admin'''
        try:
            if str(user_id) in datos.keys():
                usuario = datos[str(user_id)]
                data = request.get_json()
                usuario.update(data)
                return 'Información actualizada con éxito', 201
        except:
            abort(404, 'No se ha podido actualizar el usuario de id {}'.format(user_id))

    def delete(self, user_id):
        '''DELETE -> Rol Admin'''

        try:
            if datos[user_id]:
                del datos[(user_id)]
                return ('Usuario de id {} eliminado'.format(user_id), 204)
        except:
            abort(404, 'No se ha encontrado el usuario de id {}'.format(user_id))
            

class UsuariosAlumnos(Resource):

    def get(self):
        '''GET -> Admin, Profesor'''
        try:
                return datos
        except:
            abort(404, 'Usuarios no encontrados.')
          
    
    def post(self):
        '''POST -> Rol admin'''
        try:
            informacion = request.get_json()
            id = str(int(max(datos.keys())) + 1)
            datos[id] = informacion
            return datos[id], 201

        except:
           abort(404, 'Error al crear el usuario')
       

class UsuarioAlumno(Resource):

    def delete(self, user_id):
        '''DELETE -> Rol Admin, Profesor'''
        try:
            if datos[user_id]:
                del datos[(user_id)]
                return ('Usuario de id {} eliminado'.format(user_id), 201)
        except:
            abort(404, 'No se ha encontrado el usuario de id {}'.format(user_id))


    def put(self, user_id):
        '''PUT -> Admin, Profesor'''
        try:
          if str(user_id) in datos.keys():
              usuario = datos[str(user_id)]
              data = request.get_json()
              usuario.update(data)
              return 'Información actualizada con éxito', 201
        except:
                    abort(404, 'No se ha podido actualizar el usuario de id {}'.format(user_id))


    def get(self, user_id):

        try:
            if datos[user_id]:
                return datos[(user_id)]
        except:
            abort(404, f'no se ha encontrado el usuario de id {user_id}.')


class UsuarioProfesor(Resource):
    
    def get(self, user_id):
      'GET: Obtener listado de usuarios. Rol: ADMIN, PROFESOR'
      try:
          if datos[str(user_id)]:
              return datos[(user_id)]
      except:
          abort(404, '')
          
    def put(self, user_id):

        try:
          if str(user_id) in datos:
            usuario = datos[str(user_id)]
            data = request.get_json()
            usuario.update(data)
            return 'Éxito', 201
           
        except:
            abort(404, 'Error al crear el usuario')



datos ={
  "0": {
    "nombre": "test",
    "apellido": "test",
    "edad": 20,
    "email": "test",
    "telefono": "+549110000000000",
    "estado" : "activo",
    "rol": "admin"
  },
    "1": {
      "nombre": "Juan",
      "apellido": "Pérez",
      "edad": 25,
      "email": "juan.perez@gmail.com",
      "telefono": "+5491155555555",
      "estado" : "activo",
      "rol": "prof"
    },
    "2": {
      "nombre": "María",
      "apellido": "González",
      "edad": 30,
      "email": "maria.gonzalez@hotmail.com",
      "telefono": "+5491166666666",
      "estado" : "activo",
      "rol": "alumno"
    },
    "3": {
      "nombre": "Pedro",
      "apellido": "Rodríguez",
      "edad": 40,
      "email": "pedro.rodriguez@yahoo.com.ar",
      "telefono": "+5491177777777",
      "estado" : "activo",
      "rol": "alumno"
    },
    "4": {
      "nombre": "Lucía",
      "apellido": "Sánchez",
      "edad": 28,
      "email": "lucia.sanchez@gmail.com",
      "telefono": "+5491188888888",
      "estado" : "activo",
      "rol": "alumno"
    },
    "5": {
      "nombre": "Alejandro",
      "apellido": "Martínez",
      "edad": 35,
      "email": "alejandro.martinez@hotmail.com",
      "telefono": "+5491199999999",
      "estado" : "activo",
      "rol": "alumno"
    },
    "6": {
      "nombre": "Carolina",
      "apellido": "Gómez",
      "edad": 32,
      "email": "carolina.gomez@yahoo.com.ar",
      "telefono": "+5491167676767",
      "estado" : "activo",
      "rol": "alumno"
    },
    "7": {
      "nombre": "Santiago",
      "apellido": "García",
      "edad": 29,
      "email": "santiago.garcia@gmail.com",
      "telefono": "+5491156565656",
      "estado" : "activo",
      "rol": "alumno"
    },
    "8": {
      "nombre": "Valentina",
      "apellido": "López",
      "edad": 27,
      "email": "valentina.lopez@hotmail.com",
      "telefono": "+5491145454545",
      "estado" : "activo",
      "rol": "alumno"
    },
    "9": {
      "nombre": "Joaquín",
      "apellido": "Fernández",
      "edad": 33,
      "email": "joaquin.fernandez@yahoo.com.ar",
      "telefono": "+5491174747474",
      "estado" : "activo",
      "rol": "alumno"
    },
    "10": {
      "nombre": "Ana",
      "apellido": "Pereira",
      "edad": 26,
      "email": "ana.pereira@gmail.com",
      "telefono": "+5491136363636",
      "estado" : "activo",
      "rol": "alumno"
    },
    "11": {
      "nombre": "Matías",
      "apellido": "Rojas",
      "edad": 31,
      "email": "matias.rojas@hotmail.com",
      "telefono": "+5491162626262",
      "estado" : "activo",
      "rol": "alumno"
    },
    "12": {
      "nombre": "Florencia",
      "apellido": "Sosa",
      "edad": 29,
      "email": "florencia.sosa@yahoo.com.ar",
      "telefono": "+5491157575757",
      "estado" : "activo",
      "rol" : "alumno"
    },
    "13": {
      "nombre": "Lucas",
      "apellido": "Silva",
      "edad": 34,
      "email": "lucas.silva@gmail.com",
      "telefono": "+5491168686868",
      "estado" : "activo",
      "rol": "prof"
    },
    "14": {
      "nombre": "Brenda",
      "apellido": "Giménez",
      "edad": 28,
      "email" : "brenda_gamer@gmail.com",
      "telefono" : "+549116868685",
      "estado" : "activo",
      "rol": "alumno"
    }
}