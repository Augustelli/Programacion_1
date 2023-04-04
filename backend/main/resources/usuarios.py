from flask_restful import Resource
from flask import request, abort
import json

#Se recibe un JSON -> {key : value}
#Roles ? Valor del JSON?

with open('json_ex.json') as JSON:
    datos = json.load(JSON)


class Usuarios(Resource):
    '''Colección de usurios'''

    #Como aplicar roles

    def obtener_lista_usuarios(self):
        '''GET -> Rol admin'''
        return datos

    def crear_usuario(self):
        '''POST -> Rol admin'''
        try:
            informacion = request.get_json()
            id = int(max(datos.keys())) + 1
            datos[id] = informacion
            return datos[id], 201

        except:
            abort(404, 'Error al crear el usuario')


class Usuario(Resource):
    '''Recurso de Usuario '''

    def obterner_usuario(self, user_id):
        '''GET -> Rik Admin'''
        try:
            if int(user_id) in datos.keys():
                return datos[int(user_id)]
        except:
            abort(404, 'No se ha encontrado el usuario de ID {}'.format(user_id))



    def  editar_usuario(self, user_id ):
        '''PUT -> Rol Admin'''
        try:
            if int(user_id) in datos.keys():
                usuario = datos[int(user_id)]
                informacion = request.get_json()
                usuario.update(informacion)
                return 'Información actualizada con éxito', 201
        except:
            abort(404, 'No se ha podido actualizar el usuario de id {}'.format(user_id))

    def eliminar_alumno(self, user_id):
        '''DELETE -> Rol Admin'''

        try:
            if int(user_id) in datos.keys():
                del datos[int(user_id)]
                return ('Usuario de id {} eliminado'.format(user_id), 201)
        except:
            abort(404, 'No se ha encontrado el usuario de id {}'.format(user_id))
            

class UsuarioAlumnos(Resource):

    def obtener_listado_usuarios(self, user_id = None):
        '''GET -> Admin, Profesor'''
        try:
            if int(user_id) in datos.keys():
                return datos[user_id]
            elif user_id == None:
                return datos
        except:
            abort(404, 'Usuario no encontrado')
            


    def crear_usuario(self):
        '''POST -> Admin, profesor'''
        try:
            informacion = request.get_json()
            id = int(max(datos.keys())) + 1
            datos[id] = informacion
            return datos[id], 201

        except:
            abort(404, 'Error al crear el usuario')

            


    def eliminar_usuario_alumno(self, user_id):
        '''DELETE -> Rol Admin, Profesor'''
        try:
            if int(user_id) in datos.keys():
                del datos[int(user_id)]
                return ('Usuario de id {} eliminado'.format(user_id), 201)
        except:
            abort(404, 'No se ha encontrado el usuario de id {}'.format(user_id))


    def cambiar_estado_alumno(self, user_id, nuevo_estado):
        '''PUT -> Admin, Profesor'''
        try:
            if int(user_id) in datos.keys():
                datos[int(user_id)].update(request.get_json())

        except:
            abort(404, 'No se ha podido cambiar el estado del alumno')
            
                


class UsuarioProfesor(Resource):
    def obtener_listado_alumnos(self):
        'GET: Obtener listado de usuarios. Rol: ADMIN, PROFESOR'
        return datos.key("alumno")
            
    def crear_usuario(self):
        'POST: Crear un usuario. Rol: ADMIN, PROFESOR'
        try:
            informacion = request.get_json()
            id = int(max(datos.keys())) + 1
            datos[id] = informacion
            return datos[id], 201
        except:
            abort(404, 'Error al crear el usuario')


class UsuarioAlumno(Resource):
    'GET: . Obtener un usuario alumno. Rol: ADMIN, PROFESOR'
    
    
    'PUT: Editar un usuario alumno. Rol: ADMIN, PROFESOR'
    
    'DELETE: Eliminar un usuario alumno (cambiar de estado o suspender). Rol: ADMIN, PROFESOR'

    pass

class PlanificacionAlumno(Resource):
    'GET: Obtener las planificaciones por un alumno. Rol: ADMIN, PROFESOR, ALUMNO'
    pass

class PlanificacionesProfesores(Resource):
    'GET: Obtener las planificaciones. Rol: ADMIN, PROFESOR'
    'POST: Crear planificaciones. Rol: ADMIN, PROFESOR'

    pass

class PlanificacionProfesor(Resource):
    'GET: Obtener una planificación. Rol: ADMIN, PROFESOR'
    'PUT: Editar una planificación. Rol: ADMIN, PROFESOR'
    'DELETE: Eliminar o cambiar de estado una planificación. Rol: ADMIN, PROFESOR'
    pass

class ProfesorClases(Resource):
    'GET: Obtener un listado de profesores con clases. Rol: cualquiera'
    pass

class Pago(Resource):
    'GET: Obtener pago por alumno. Rol: ADMIN, PROFESOR'
    'PUT: Actualizar el estado del pago. Rol: ADMIN, PROFESOR'
    pass

class Login(Resource):
    'POST: crea el acceso a la app. Rol: cualquiera'
    pass