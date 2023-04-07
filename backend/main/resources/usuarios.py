from flask_restful import Resource
from flask import request, abort
import json

#Se recibe un JSON -> {key : value}
#Roles ? Valor del JSON?

with open('main/resource/json_ex.json') as JSON:
    datos = json.load(JSON)


class Usuarios(Resource):
    '''Colección de usurios'''

    #Como aplicar roles

    def obtener_listado_usuarios(self):
        '''GET -> Rol admin'''
        return datos


    def crear_usuario(self,data):
        '''POST -> Rol admin'''
        try:
            informacion = data
            id = str(int(max(datos.keys())) + 1)
            datos[id] = informacion
            return datos[id], 201

        except:
            abort(404, 'Error al crear el usuario')


class Usuario(Resource):
    '''Recurso de Usuario '''

    def obterner_usuario(self, user_id):
        '''GET -> Rik Admin'''
        try:
            if datos[user_id]:
                return datos[(user_id)]
        except:
            abort(404, '')


    def  editar_usuario(self, user_id, data ):
        '''PUT -> Rol Admin'''
        try:
            if datos[user_id]:
                usuario = datos[(user_id)]
                usuario.update(data)
                return 'Información actualizada con éxito', 201
        except:
            abort(404, 'No se ha podido actualizar el usuario de id {}'.format(user_id))

    def eliminar_alumno(self, user_id):
        '''DELETE -> Rol Admin'''

        try:
            if datos[user_id]:
                del datos[(user_id)]
                return ('Usuario de id {} eliminado'.format(user_id), 201)
        except:
            abort(404, 'No se ha encontrado el usuario de id {}'.format(user_id))
            

class UsuarioAlumnos(Resource):

    def obtener_listado_usuarios(self, user_id = None):
        '''GET -> Admin, Profesor'''
        try:
            if datos[user_id]:
                return datos[user_id]
            elif user_id == None:
                return datos
        except:
            abort(404, 'Usuario no encontrado')
            


    def crear_usuario(self,data):
        '''POST -> Admin, profesor'''
        try:
            id = str(int(max(datos.keys())) + 1)
            datos[id] =  data
            return datos[id], 201

        except:
            abort(404, 'Error al crear el usuario')

class UsuarioAlumno(Resource):

    def eliminar_usuario_alumno(self, user_id):
        '''DELETE -> Rol Admin, Profesor'''
        try:
            if datos[user_id]:
                del datos[(user_id)]
                return ('Usuario de id {} eliminado'.format(user_id), 201)
        except:
            abort(404, 'No se ha encontrado el usuario de id {}'.format(user_id))


    def cambiar_estado_alumno(self, user_id, nuevo_estado):
        '''PUT -> Admin, Profesor'''
        try:
            if datos[user_id]:
                datos[int(user_id)].update(request.get_json())

        except:
            abort(404, 'No se ha podido cambiar el estado del alumno')
            
    def obtener_usuario_alumno(self, user_id):

        try:
            if datos[user_id]:
                return datos[(user_id)]
        except:
            abort(404, f'no se ha encontrado el usuario de id {user_id}.')


class UsuarioProfesor(Resource):
    
    def obtener_listado_alumnos(self):
        'GET: Obtener listado de usuarios. Rol: ADMIN, PROFESOR'
        return datos.key("alumno")
            
    def crear_usuario(self, data):
        'POST: Crear un usuario. Rol: ADMIN, PROFESOR'
        try:
            id = str(int(max(datos.keys())) + 1)
            datos[id] = data
            return datos[id], 201
        except:
            abort(404, 'Error al crear el usuario')

    def editar_usuario_alumno(self, user_id, data):
        try:
            if datos[user_id]:
                usuario = datos[(user_id)]
                usuario.update(data)
                return 'Información actualizada con éxito', 201
        except:
            abort(404, 'Error al actualizar el usuario')

