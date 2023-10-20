from flask_restful import Resource
from flask import request
from .. import db
from main.models import UsuarioModelo, AlumnoModel, ProfesorModelo,ClasesModelo, PagosModelo
from flask_jwt_extended import jwt_required, get_jwt_identity  # noqa
from main.auth.decorators import role_required
import datetime
import pdb  # noqa
# from ..mail import sendMail

class Usuarios(Resource):

    # Rol : Admin
    @role_required(roles=['admin','profesor'])
    def get(self):

        try:
            page = 1
            per_page = 10

            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            usuarios = db.session.query(UsuarioModelo)

             
            for usuario in usuarios:
                payments = PagosModelo.query.filter_by(dni=usuario.dni).all()
                if not payments:  # Check if there are no payments for the user
                    usuario.estado = False
                    db.session.commit()
                for payment in payments:
                    current_time = datetime.datetime.now()
                    # print(usuario.dni, payment.fecha_de_pago)
                    if payment.fecha_de_pago <= current_time:
                        usuario.estado = False
                        db.session.commit()
                    else:
                        usuario.estado = True
                        db.session.commit()


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

    # Rol: Admin
    @role_required(roles=['admin', 'profesor'])
    def post(self):
        try:
            campos_obligatorios = {'dni', 'nombre', 'apellido', 'email', 'contrasegna'}
            datos = request.get_json()
            campos_recibidos = set(datos.keys())

            campos_faltantes = campos_obligatorios - campos_recibidos
            if campos_faltantes:
                raise Exception(
                    f'Error al crear usuario. Faltan campos obligatorios: {campos_faltantes}. Por favor, incluya estos campos y vuelva a intentarlo.')

            for campo in campos_obligatorios:
                if datos[campo] is None:
                    raise Exception(f'Error al crear usuario. El campo {campo} no puede ser nulo. Por favor, proporcione un valor válido para {campo} y vuelva a intentarlo.')  # noqa

            usuario_nuevo = UsuarioModelo.from_json(datos)
            # db.session.add(usuario_nuevo)
            if usuario_nuevo.rol == "alumno":

                alumno_usuario = UsuarioModelo(
                    dni=usuario_nuevo.dni,
                    nombre=usuario_nuevo.nombre,
                    apellido=usuario_nuevo.apellido, 
                    email=usuario_nuevo.email, 
                    fecha_nacimiento=usuario_nuevo.fecha_nacimiento,
                    estado = usuario_nuevo.estado,
                    contrasegna=usuario_nuevo.contrasegna,
                    nombre_usuario=usuario_nuevo.nombre_usuario,
                    rol=usuario_nuevo.rol)
                altura = datos["altura"] if "altura" in datos else None
                peso = datos["peso"] if "peso" in datos else None
                db.session.add(alumno_usuario)

                alumno = AlumnoModel(
                    alumno_dni=usuario_nuevo.dni, 
                    altura=altura, 
                    peso=peso)
                db.session.add(alumno)
            if usuario_nuevo.rol == "profesor":

                salario = datos['salario'] if "salario" in datos else None
                especialidad = datos['especialidad'] if 'especialidad' in datos else None
                profesor_usuario = UsuarioModelo(dni=usuario_nuevo.dni, nombre=usuario_nuevo.nombre, apellido=usuario_nuevo.apellido, email=usuario_nuevo.email, contrasegna=usuario_nuevo.contrasegna, rol=usuario_nuevo.rol,fecha_nacimiento=usuario_nuevo.fecha_nacimiento, estado=True, nombre_usuario=usuario_nuevo.nombre_usuario)
                db.session.add(profesor_usuario)
                profesor = ProfesorModelo(
                    profesor_dni=usuario_nuevo.dni, 
                    especialidad=especialidad, 
                    salario=salario)
                db.session.add(profesor)
                if 'idClase' in datos:
                    id_clase = datos['idClase']
                    id_profesor = db.session.query(ProfesorModelo).filter_by(profesor_dni=usuario_nuevo.dni).first().idProfesor
                    try:
                        clase = db.session.query(ClasesModelo).filter_by(idClases=id_clase).first()

                        profesor = db.session.query(ProfesorModelo).filter_by(idProfesor=id_profesor).first()
                        clase.profesores.append(profesor)
                        db.session.commit()
                    except Exception as e:
                        return {'error': 'No existe esa clase'}, 400


            if usuario_nuevo.rol == "admin":
                usuario=UsuarioModelo(
                    dni=usuario_nuevo.dni,
                    nombre=usuario_nuevo.nombre,
                    apellido=usuario_nuevo.apellido, 
                    email=usuario_nuevo.email, 
                    fecha_nacimiento=usuario_nuevo.fecha_nacimiento,
                    estado = usuario_nuevo.estado,
                    contrasegna=usuario_nuevo.contrasegna,
                    nombre_usuario=usuario_nuevo.nombre_usuario,
                    rol=usuario_nuevo.rol)
                db.session.add(usuario)

            db.session.commit()
            # sent = sendMail([usuario_nuevo.email], "Bienvenido a la plataforma del gimnasio del Grupo D, hay una nueva planificación disponible", "register", )
            return usuario_nuevo.to_json(), 201
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

class Usuario(Resource):

    # Rol: Admin
    @role_required(roles=['admin', 'profesor','alumno'])
    def get(self):
        try:
            page = 1
            per_page = 10

            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))

            usuarios = db.session.query(UsuarioModelo)
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

    # Rol: Admin
    @role_required(roles=['admin', 'profesor'])
    def put(self):
        try:
            if request.args.get('nrDni'):
                registro = db.session.query(UsuarioModelo).get(request.args.get('nrDni'))
                registro1 = db.session.query(AlumnoModel).get(request.args.get('nrDni'))
                if registro:
                    pass
                else:
                    raise Exception(f"No se ha encontrado usuario con DNI: {(request.args.get('nrDni'))}")
                
                usuario_editar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == int(request.args.get('nrDni'))).first()
                
                usuario_editar1 = db.session.query(AlumnoModel).filter(AlumnoModel.alumno_dni == int(request.args.get('nrDni'))).first()
                usuario_editar2 = db.session.query(ProfesorModelo).filter(ProfesorModelo.profesor_dni == int(request.args.get('nrDni'))).first()
                informacion = request.get_json().items()
                for campo, valor in informacion:
                    # if campo == 'dni':

                    # if campo == 'rol':
                    #     raise Exception('El rol del usuario no puede ser modificado.')

                    setattr(usuario_editar, campo, valor)
                    if campo == 'peso':
                        usuario_editar1.peso = float(valor)
                        db.session.add(usuario_editar1)
                    if campo == 'altura':
                        usuario_editar1.altura = float(valor)
                        db.session.add(usuario_editar1)
                    if campo == 'dni' and usuario_editar.rol == 'alumno':
                        usuario_editar1.alumno_dni = int(valor)
                        db.session.add(usuario_editar1)
                    if campo == 'salario':
                        usuario_editar2.salario = float(valor)
                        db.session.add(usuario_editar2)
                    if campo == 'especialidad':
                        usuario_editar2.especialidad = valor
                        db.session.add(usuario_editar2)
                    if campo == 'dni' and usuario_editar.rol == 'profesor':
                        usuario_editar2.profesor_dni = int(valor)
                        db.session.add(usuario_editar2)

                db.session.add(usuario_editar)
                db.session.commit()
                return usuario_editar.to_json(), 201
            else:
                raise Exception('El DNI del usuario es necesario para poder modificarlo.')
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

    @role_required(roles=['admin'])
    def delete(self):
        try:
            dni = request.args.get('nrDni')
            if dni:
                usuario_eliminar = db.session.query(UsuarioModelo).filter_by(dni=dni).first()
                if usuario_eliminar:
                    db.session.delete(usuario_eliminar)

                    alumno_eliminar = db.session.query(AlumnoModel).get(dni)
                    if alumno_eliminar:
                        db.session.delete(alumno_eliminar)

                    db.session.commit()
                    return 'Usuario eliminado correctamente', 200

                else:
                    raise Exception(f"No se ha encontrado usuario con DNI: {dni}")
            else:
                raise Exception("El DNI del usuario debe ser especificado para eliminarlo")
        except Exception as e:
            db.session.rollback()
            return {
                'Error': str(e)
            }, 400
        finally:
            db.session.close()


class UsuarioAlumnos(Resource):

    # Rol Admin, profesor
    @role_required(roles=['admin', 'profesor'])
    def get(self):
        page = 1
        per_page = 10

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        usuarios = db.session.query(UsuarioModelo )
        usuarios = usuarios.outerjoin(AlumnoModel, UsuarioModelo.dni == AlumnoModel.alumno_dni)
        usuarios = usuarios.filter(UsuarioModelo.rol == 'alumno')
        # usuarios = query.filter(UsuarioModelo.dni == request.args.get('nrAlumno'))

        usuarios_paginados = usuarios.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
        usuarios_json = [usuario.to_json() for usuario in usuarios_paginados.items]

        return {
                'Usuario': usuarios_json,
                'Pagina': page,
                'Por pagina': per_page,
                'Total': usuarios_paginados.total
                }

    @role_required(roles=['admin'])
    def post(self):
        try:
            campos_obligatorios = {'dni', 'nombre', 'apellido', 'email', 'contrasegna'}
            datos = request.get_json()
            campos_recibidos = set(datos.keys())

            campos_faltantes = campos_obligatorios - campos_recibidos
            if campos_faltantes:
                raise Exception(
                    f'Error al crear alumno. Faltan campos obligatorios: {campos_faltantes}. Por favor, incluya estos campos y vuelva a intentarlo.')

            for campo in campos_obligatorios:
                if datos[campo] is None:
                    raise Exception(
                        f'Error al crear alumno. El campo {campo} no puede ser nulo. Por favor, proporcione un valor válido para {campo} y vuelva a intentarlo.')  # noqa

            usuario_nuevo = UsuarioModelo.from_json(datos)
            db.session.add(usuario_nuevo)
            alumno = AlumnoModel(alumno_dni=usuario_nuevo.dni)
            db.session.add(alumno)
            db.session.commit()
            #sent=
            return usuario_nuevo.to_json(), 201
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()


class UsuarioProfesor(Resource):

    # Rol admin, Profesor
    @role_required(roles=['admin', 'profesor', 'alumno','espera'])
    def get(self):
        try:
            profesores = db.session.query(UsuarioModelo, ProfesorModelo).\
                join(ProfesorModelo, UsuarioModelo.dni == ProfesorModelo.profesor_dni)

            page = 1
            per_page = 10

            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))

            if request.args.get('nrDni'):
                profesores = profesores.filter(UsuarioModelo.dni == request.args.get('nrDni'))


            profesores_paginados = profesores.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)

            # Construir la respuesta
            profesores_json = []
            for usuario, profesor in profesores_paginados.items:
                profesor_data = {
                    'dni': usuario.dni,
                    'rol': usuario.rol,
                    'nombre': usuario.nombre,
                    'apellido': usuario.apellido,
                    'email': usuario.email,
                    'idProfesor': profesor.idProfesor,
                    'especialidad': profesor.especialidad,
                    'salario': profesor.salario
                }
                profesores_json.append(profesor_data)

            return {
                'Usuario': profesores_json,
                'Pagina': page,
                'Por pagina': per_page,
                'Total': profesores_paginados.total
            }
        except Exception as e:
            return {'error': str(e)}, 404
        finally:
            db.session.close()


    @role_required(roles=['admin', 'profesor'])
    def put(self):
        try:
            if request.args.get('nrDni'):
                registro = db.session.query(UsuarioModelo).get(request.args.get('nrDni'))
                registro1 = db.session.query(ProfesorModelo).get(request.args.get('nrDni'))
                if registro:
                    pass
                else:
                    raise Exception(f"No se ha encontrado usuario con DNI: {(request.args.get('nrDni'))}")
                usuario_editar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == int(request.args.get('nrDni'))).first()
                usuario_editar1 = db.session.query(ProfesorModelo).filter(ProfesorModelo.profesor_dni == int(request.args.get('nrDni'))).first()
                informacion = request.get_json().items()
                for campo, valor in informacion:
                    if campo == 'rol':
                        raise Exception('El rol del usuario no puede ser modificado.')

                    if campo == 'salario' :
                        usuario_editar1.salario = float(valor)
                        db.session.add(usuario_editar1)
                    
                    if campo == 'especialidad':
                        usuario_editar1.especialidad = valor
                        db.session.add(usuario_editar1)
                    if campo == 'dni':
                        usuario_editar1.profesor_dni = int(valor)
                        db.session.add(usuario_editar1)

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

    
        #       
        #         for campo, valor in informacion:
        #             # if campo == 'dni':

        #             # if campo == 'rol':
        #             #     raise Exception('El rol del usuario no puede ser modificado.')

        #             setattr(usuario_editar, campo, valor)
        #             if campo == 'peso':
        #                 usuario_editar1.peso = float(valor)
        #                 db.session.add(usuario_editar1)
        #             if campo == 'altura':
        #                 usuario_editar1.altura = float(valor)
        #                 db.session.add(usuario_editar1)
        #             if campo == 'dni':
        #                 usuario_editar1.alumno_dni = int(valor)
        #                 db.session.add(usuario_editar1)
        #         db.session.add(usuario_editar)
        #         db.session.commit()
        #         return usuario_editar.to_json(), 201
        #     else:
        #         raise Exception('El DNI del usuario es necesario para poder modificarlo.')
        # except Exception as e:
        #     return {'error': str(e)}, 400
        # finally:
        #     db.session.close()


class UsuarioAlumno(Resource):



    #   
    #        
    @role_required(roles=['admin', 'profesor', 'alumno'])
    def get(self):
        
        try:
            usuarios = db.session.query(UsuarioModelo, AlumnoModel).join(AlumnoModel, UsuarioModelo.dni == AlumnoModel.alumno_dni)
            page = 1
            per_page = 10

            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))

            if request.args.get('nrDni'):
                usuarios = usuarios.filter(UsuarioModelo.dni == request.args.get('nrDni'))

            usuarios_paginados = usuarios.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)

            # Construir la respuesta
            usuarios_json = []
            for usuario, alumno in usuarios_paginados.items:
                usuario_data = {
                    'dni': usuario.dni,
                    'id':alumno.idAlumno,
                    'rol': usuario.rol,
                    'nombre': usuario.nombre,
                    'apellido': usuario.apellido,
                    'email': usuario.email,
                    'altura': alumno.altura,
                    'peso': alumno.peso
                }
                usuarios_json.append(usuario_data)

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


             
    #            
    #             

    #               

    #                 setattr(usuario_editar, campo, valor)

    #             db.session.add(usuario_editar)

    #             db.session.commit()
    #             return usuario_editar.to_json(), 201
    #         else:
    #             raise Exception('El DNI del usuario es necesario para poder modificarlo.')
    #     except Exception as e:
    #         return {'error': str(e)}, 400
    #     finally:

    # Rol Admin, Profesor


    @role_required(roles=['admin', 'profesor'])
    def put(self):
        try:
            if request.args.get('nrDni'):
                registro = db.session.query(UsuarioModelo).get(request.args.get('nrDni'))
                registro1 = db.session.query(AlumnoModel).get(request.args.get('nrDni'))
                
                if registro:
                    pass
                else:
                    raise Exception(f"No se ha encontrado alumno con DNI: {(request.args.get('nrDni'))}")
                
                usuario_editar = db.session.query(UsuarioModelo).filter(UsuarioModelo.dni == int(request.args.get('nrDni'))).first()
                usuario_editar1 = db.session.query(AlumnoModel).filter(AlumnoModel.alumno_dni == int(request.args.get('nrDni'))).first()
                print("usuario a editar",usuario_editar1)

                informacion = request.get_json().items()
                for campo, valor in informacion:
                    if campo == 'rol':
                        raise Exception('El rol del usuario no puede ser modificado.')
                    
                    if campo == "peso":
                        usuario_editar1.peso = float(valor)
                        db.session.add(usuario_editar1)
                    if campo == "altura":
                        usuario_editar1.altura = float(valor)
                        db.session.add(usuario_editar1)
                    if campo == "dni":
                        usuario_editar1.alumno_dni = int(valor)
                        db.session.add(usuario_editar1)


                    setattr(usuario_editar, campo, valor)
                db.session.add(usuario_editar)
                db.session.commit()
                return usuario_editar.to_json(), 201
            else:
                raise Exception('El DNI del alumno es necesario para poder modificarlo.')
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

    @role_required(roles=['admin', 'profesor'])
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


class UsuariosLogin(Resource):

    # Rol : Admin
    def get(self):
        try:
            

            usuarios = db.session.query(UsuarioModelo)
            if request.args.get('nrDni'):
                usuarios = usuarios.filter(UsuarioModelo.dni == int(request.args.get('nrDni')))
            if request.args.get('email'):
                usuarios = usuarios.filter(UsuarioModelo.email == request.args.get('email'))
            
            usuarios_json = [usuario.to_json() for usuario in usuarios.all()]


           

            return usuarios_json
                                

        except Exception as e:
            return {'error': str(e)}, 404
        finally:
            db.session.close()