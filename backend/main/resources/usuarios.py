from flask_restful import Resource
from flask import request, abort, jsonify
from .. import db
from main.models import UsuarioModelo, AlumnoModel, ProfesorModelo
from sqlalchemy import or_
import pdb
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Usuarios(Resource):
    @jwt_required(optional=True)
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
    @role_required(roles="admin")
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
            if usuario_nuevo.rol == "alumno":
                alumno = AlumnoModel(alumno_dni=usuario_nuevo.dni)
                db.session.add(alumno)
            if usuario_nuevo.rol == "profesor":
                if "salario" in datos:
                    salario = datos["salario"]
                else:
                    salario = None

                if "especialidad" in datos:
                    especialidad = datos["especialidad"]
                else:
                    especialidad = None

                profesor = ProfesorModelo(profesor_dni=usuario_nuevo.dni, especialidad=especialidad, salario=salario)
                db.session.add(profesor)

            db.session.commit()
            return usuario_nuevo.to_json(), 201
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()
    @role_required(roles=["admin","profesor"])
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
                    if campo == 'rol':
                        raise Exception('El rol del usuario no puede ser modificado.')
                    
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
    @role_required(roles="admin")
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


