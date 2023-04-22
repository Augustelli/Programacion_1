from flask_restful import Resource
from flask import request, abort, jsonify
from main import db
from main.models import UsuarioModelo
from sqlalchemy import or_


class Usuarios(Resource):

    # Como aplicar roles
    # Devolver listado de alumnos
    def get(self):

        try:
            usuarios = db.session.usuario(UsuarioModelo).all()
            return jsonify(usuario.to_json() for usuario in usuarios)

        except Exception:
            abort(404, 'Query no encontrado')
        finally:
            db.session.close()

    def post(self):
        # Crear un usuario
        try:
            usuario_nuevo = UsuarioModelo.from_json(request.get_json())
            db.session.add(usuario_nuevo)
            db.session.commit()
            return usuario_nuevo.to_json(), 201

        except BaseException:
            abort(404, 'Error al crear el usuario')
        finally:
            db.session.close()


class Usuario(Resource):

    def get(self, user_id):
        try:
            usuario_rescatado = db.session.query(UsuarioModelo).filter(
                UsuarioModelo.idUsuario == user_id,).first()
            return usuario_rescatado.to_json(), 201
        except Exception:
            abort(404, f'No se ha encontrado del usuario de id: {user_id}')
        finally:
            db.session.close()

    def put(self, user_id):

        try:
            usuario_editar = db.session.query(UsuarioModelo).filter(UsuarioModelo.idUsuario == user_id).first()
            informacion = request.get_json().items()
            for campo, valor in informacion:
                setattr(usuario_editar, campo, valor)
            db.session.add(usuario_editar)
            db.session.commit()
            return usuario_editar.to_json(), 201
        except BaseException:
            abort(404, 'No se ha podido actualizar el usuario de id {}'.format(user_id))
        finally:
            db.session.close()

    def delete(self, user_id):

        try:
            usuario_eliminar = db.session.query(UsuarioModelo).filter(UsuarioModelo.idUsuario == user_id).first()
            db.session.delete(usuario_eliminar)
            db.session.commit()
            return 204
        except BaseException:
            abort(404, 'No se ha encontrado el usuario de id {}'.format(user_id))
        finally:
            db.session.close()


class UsuariosAlumnos(Resource):

    def get(self):
        '''GET -> Admin, Profesor'''
        try:
          return datos
        except BaseException:
            abort(404, 'Usuarios no encontrados.')

    def post(self):
        '''POST -> Rol admin'''
        try:
            informacion = request.get_json()
            id = str(int(max(datos.keys())) + 1)
            datos[id] = informacion
            return datos[id], 201

        except BaseException:
          abort(404, 'Error al crear el usuario')
       

class UsuarioAlumno(Resource):

    def delete(self, user_id):
        '''DELETE -> Rol Admin, Profesor'''
        try:
            if datos[user_id]:
                del datos[(user_id)]
                return ('Usuario de id {} eliminado'.format(user_id), 201)
        except BaseException:
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
        except BaseException:
            abort(404, f'no se ha encontrado el usuario de id {user_id}.')


class UsuarioProfesor(Resource):
    
    def get(self, user_id):
      '''GET: Obtener listado de usuarios. Rol: ADMIN, PROFESOR'''
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


