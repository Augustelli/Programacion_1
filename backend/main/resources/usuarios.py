from flask_restful import Resource
from flask import request, abort, jsonify
from .. import db
from main.models import UsuarioModelo, AlumnoModel, ProfesorModelo
from sqlalchemy import or_
import pdb


class Usuarios(Resource):
    def get(self):
        try:
            usuarios = db.session.query(UsuarioModelo)
            page = 1
            per_page = 10

            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))

            if request.args.get('nrRol'):
                usuarios = usuarios.filter(UsuarioModelo.rol.like("%"+request.args.get('nrRol')+"%"))

            if request.args.get('nrProfesor'):
                query = usuarios.outerjoin(ProfesorModelo, UsuarioModelo.dni == ProfesorModelo.profesor_dni)
                usuarios = query.filter(UsuarioModelo.dni == request.args.get('nrProfesor'))

            if request.args.get('nrAlumno'):
                query = usuarios.outerjoin(AlumnoModel, UsuarioModelo.dni == AlumnoModel.alumno_dni)
                usuarios = query.filter(UsuarioModelo.dni == request.args.get('nrAlumno'))

            if request.args.get('nrDni'):
                usuarios = usuarios.filter(UsuarioModelo.dni == int(request.args.get('nrDni')))

            usuarios_paginados = usuarios.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            usuarios_json = [usuario.to_json() for usuario in usuarios_paginados.items]

            return {
                'Usuario': usuarios_json,
                'Pagina': page,
                'Por pagina': per_page,
                'Total': usuarios_paginados.total
            }
        except Exception as e:
            return {'error': str(e)}, 404
        finally:
            db.session.close()

    def post(self):
        try:
            campos_obligatorios = {'dni', 'nombre', 'apellido', 'email', 'contrasegna'}
            datos = request.get_json()
            campos_recibidos = set(datos.keys())

            campos_faltantes = campos_obligatorios - campos_recibidos
            if campos_faltantes:
                raise Exception(f'Error al crear usuario. Faltan campos obligatorios: {campos_faltantes}. Por favor, incluya estos campos y vuelva a intentarlo.')

            for campo in campos_obligatorios:
                if datos[campo] is None:
                    raise Exception(f'Error al crear usuario. El campo {campo} no puede ser nulo. Por favor, proporcione un valor válido para {campo} y vuelva a intentarlo.')

            usuario_nuevo = UsuarioModelo.from_json(datos)
            db.session.add(usuario_nuevo)
            db.session.commit()
            return usuario_nuevo.to_json(), 201
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

    def put(self):

        try:
            if request.args.get('nrDni'):
                registro = db.session.query(UsuarioModelo).get(request.args.get('nrDni'))
                if registro:
                    pass
                else:
                    raise Exception(f"No se ha encontrado usuario con DNI: {(request.args.get('nrDni'))}")
                usuario_editar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == int(request.args.get('nrDni'))).first()
                informacion = request.get_json().items()
                for campo, valor in informacion:
                    setattr(usuario_editar, campo, valor)
                db.session.add(usuario_editar)
                db.session.commit()
                return usuario_editar.to_json(), 201
            else:
                raise Exception('El DNI del usuario es necesario para poder modificarlo.')
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

    def delete(self):
        try:
            if request.args.get('nrDni'):
                registro = db.session.query(UsuarioModelo).get(request.args.get('nrDni'))
                if registro:
                    pass
                else:
                    raise Exception(f"No se ha encontrado usuario con DNI: {(request.args.get('nrDni'))}")
                usuario_eliminar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == request.args.get('nrDni')).first()
                db.session.delete(usuario_eliminar)
                db.session.commit()
                return 204, f"Usuario de DNI {request.args.get('nrDni')} eliminado"
            else:
                raise Exception("El DNI del usuario debe ser especificado para eliminarlo")
        except Exception:
            return {
                'error': str(Exception())
            }, 400
        finally:
            db.session.close()
# SACAR recurso usuario


class Usuario(Resource):

    def get(self, user_id):
        try:
            usuario_rescatado = db.session.query(UsuarioModelo).filter(
                UsuarioModelo.dni == user_id).first()
            return usuario_rescatado.to_json(), 201
        except Exception:
            abort(404, f'No se ha encontrado del usuario de DNI: {user_id}')
        finally:
            db.session.close()

  


class UsuariosAlumnos(Resource):

    def get(self):
        try:
            alumnos = db.session.query(UsuarioModelo).filter(UsuarioModelo.rol == 'alumno').all()
            alumnos_json = [alumno.to_json() for alumno in alumnos]
            return jsonify(alumnos_json)
        except BaseException:
            abort(404, 'Alumnos no encontrados.')
        finally:
            db.session.close()

    def post(self):
        try:
            datos = request.get_json()
            if datos['dni'] == None:
                raise Exception('No se puede crear el Alumno, Falta el DNI')
        except BaseException:
            abort(404, f"")
        finally:
            db.session.close()


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
    # NO FUNCIONA @Agustelli
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
