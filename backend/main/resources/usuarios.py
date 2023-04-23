from flask_restful import Resource
from flask import request, abort, jsonify
from main import db
from main.models import UsuarioModelo, AlumnoModel, ProfesorModelo


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
        try:
            alumnos = db.session.query(AlumnoModel).all()
            return alumnos.to_json()
        except BaseException:
            abort(404, 'Usuarios no encontrados.')
        finally:
            db.session.close()

    def post(self):
        try:
            alumno_nuevo = AlumnoModel.from_json(request.get_json())
            db.session.add(alumno_nuevo)
            db.session.commit()
            return alumno_nuevo.to_json(), 201

        except BaseException:
            abort(404, 'Error al crear el alumno')
        finally:
            db.session.close()


class UsuarioAlumno(Resource):

    def delete(self, user_id):
        '''DELETE -> Rol Admin, Profesor'''
        try:
            alumno_eliminar = db.session.query(AlumnoModel).filter(AlumnoModel.idAlumno == user_id).first()
            db.session.delete(alumno_eliminar)
            db.session.commit()
            return 204
        except BaseException:
            abort(404, 'No se ha encontrado el alumno de id {}'.format(user_id))
        finally:
            db.session.close()

    def put(self, user_id):

        try:
            alumno_editar = db.session.query(AlumnoModel).filter(AlumnoModel.idAlumno == user_id).first()
            informacion = request.get_json().items()
            for campo, valor in informacion:
                setattr(alumno_editar, campo, valor)
            db.session.add(alumno_editar)
            db.session.commit()
            return alumno_editar.to_json(), 201

        except BaseException:

            abort(404, 'No se ha podido actualizar el usuario de id {}'.format(user_id))

        finally:
            db.session.close()

    def get(self, user_id):

        try:
            alumno_rescatado = db.session.query(AlumnoModel).filter(
                AlumnoModel.idAlumno == user_id,).first()
            return alumno_rescatado.to_json(), 201
        except Exception:
            abort(404, f'No se ha encontrado del alumno de id: {user_id}')
        finally:
            db.session.close()


class UsuarioProfesor(Resource):

    def get(self, user_id):

        try:
            profesor_rescatado = db.session.query(ProfesorModelo).filter(
                ProfesorModelo.idProfesor == user_id,).first()
            return profesor_rescatado.to_json(), 201
        except Exception:
            abort(404, f'No se ha encontrado del alumno de id: {user_id}')
        finally:
            db.session.close()

    def put(self, user_id):
        try:
            alumno_editar = db.session.query(AlumnoModel).filter(AlumnoModel.idAlumno == user_id).first()
            informacion = request.get_json().items()
            for campo, valor in informacion:
                setattr(alumno_editar, campo, valor)
            db.session.add(alumno_editar)
            db.session.commit()
            return alumno_editar.to_json(), 201

        except BaseException:

            abort(404, 'No se ha podido actualizar el usuario de id {}'.format(user_id))
