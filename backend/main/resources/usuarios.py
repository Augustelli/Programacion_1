from flask_restful import Resource
from flask import request, abort, jsonify
from .. import db
from main.models import UsuarioModelo, AlumnoModel, ProfesorModelo
from sqlalchemy import or_


class Usuarios(Resource):

    # Como aplicar roles
    # Devolver listado de alumnos
    def get(self):
        

        try:
            usuarios = db.session.query(UsuarioModelo).all()
            usuarios_json = [usuario.to_json() for usuario in usuarios]
            return jsonify(usuarios_json)

        except Exception:
            print('Fallo')
            abort(404, 'Query no encontrado')
        finally:
            db.session.close()

    def post(self):
      #  Crear un usuariopwd
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
                UsuarioModelo.dni == user_id).first()
            return usuario_rescatado.to_json(), 201
        except Exception:
            abort(404, f'No se ha encontrado del usuario de id: {user_id}')
        finally:
            db.session.close()

    def put(self, user_id):

        try:
            usuario_editar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == user_id).first()
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
            usuario_eliminar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == user_id).first()
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
            alumnos_json = [alumno.to_json() for alumno in alumnos]
            return jsonify(alumnos_json)
        except BaseException:
             abort(404, 'Alumnos no encontrados.')
        finally:
             db.session.close()

    def post(post):
        try:
            datos = request.get_json()
            return datos
        except Exception:
            abort(404)

        
class UsuarioAlumno(Resource):


    # def post(self,user_id):
    #     try:
    #         datos = request.get_json()

    #         usuario_nuevo = UsuarioModelo.from_json(datos)
    #         db.session.add(usuario_nuevo)
    #         dni_usuario = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == user_id).first()
    #         if datos['rol'] != 'alumno':
    #             datos['rol'] = 'alumno'
    #         alumno_nuevo = AlumnoModel(dni=dni_usuario)
    #         db.session.commit()
    #         return alumno_nuevo.to_json(), 201
    def post(self, user_id):
        try:
            datos = request.get_json()
            dni_usuario = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == user_id).first()
            usuario_nuevo = UsuarioModelo.from_json(datos)
            db.session.add(usuario_nuevo)
            if datos['rol'] != 'alumno':
                datos['rol'] = 'alumno'
            alumno_nuevo = AlumnoModel(dni=dni_usuario)
            db.session.add(alumno_nuevo)
            db.session.commit()
            return alumno_nuevo.to_json(), 201

        except BaseException:
            abort(404, 'Error al crear el alumno')
        finally:
            db.session.close()

    def delete(self, user_id):
        '''DELETE -> Rol Admin, Profesor'''
        try:
            alumno_eliminar = db.session.query(AlumnoModel).filter(or_(
                AlumnoModel.alumno_dni == user_id,
                AlumnoModel.idAlumno == user_id
            )).first()
            db.session.delete(alumno_eliminar)
            db.session.commit()
            return 204
        except BaseException:
            abort(404, 'No se ha encontrado el alumno de id {}'.format(user_id))
        finally:
            db.session.close()

    def put(self, user_id):

        try:
            alumno_editar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == user_id).first()
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
            alumno_rescatado = db.session.query(UsuarioModelo).filter(
                UsuarioModelo.dni == user_id,).first()
            return alumno_rescatado.to_json(), 201
        except Exception:
            abort(404, f'No se ha encontrado del alumno de id: {user_id}')
        finally:
            db.session.close()


class UsuarioProfesor(Resource):

#NO FUNCIONA @Agustelli
    def get(self, user_id):

        try:
            dni_profesor = db.session.query(ProfesorModelo).filter(ProfesorModelo.idProfesor == user_id)
            if dni_profesor is None:
                raise Exception('ID no pertenece a un profesor.')
            profesor_rescatado = db.session.query(UsuarioModelo).filter(UsuarioModelo.profesor_dni == user_id,).first()
            return profesor_rescatado.to_json(), 201
        except Exception:
            abort(404, f'No se ha encontrado del Profesor de id: {user_id}')
        finally:
            db.session.close()

    def put(self, user_id):
        try:
            alumno_editar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == user_id).first()
            informacion = request.get_json().items()
            for campo, valor in informacion:
                setattr(alumno_editar, campo, valor)
            db.session.add(alumno_editar)
            db.session.commit()
            return alumno_editar.to_json(), 201

        except BaseException:

            abort(404, 'No se ha podido actualizar el usuario de id {}'.format(user_id))
        

    def delete(self, user_id):
        '''DELETE -> Rol Admin, Profesor'''
        try:
            profe_eliminar = db.session.query(ProfesorModelo).filter(or_(
                    ProfesorModelo.profesor_dni == user_id,
                    ProfesorModelo.idProfesor == user_id
                )).first()
            db.session.delete(profe_eliminar)
            db.session.commit()
            return 204
        except BaseException:
            abort(404, 'No se ha encontrado el alumno de id {}'.format(user_id))
        finally:
            db.session.close()

class UsuariosProfesores(Resource):

    def get(self):
        try:
            profesores = db.session.query(ProfesorModelo).all()
            profesores_json = [profesor.to_json() for profesor in profesores]
            return jsonify(profesores_json)
        except BaseException:
             abort(404, 'Profesores no encontrados.')
        finally:
             db.session.close()

    def post(post):
        try:
            datos = request.get_json()
            return datos
        except Exception:
            abort(404)

        

        
