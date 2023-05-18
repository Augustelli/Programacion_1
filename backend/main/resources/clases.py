from flask import request, abort, jsonify
from .. import db
from main.models import ClasesModelo,clase_profesorModelo,ProfesorModelo
from flask_restful import Resource


class Clase_Profesor_R(Resource):
    def get(self):
        try:
            clase_profesor = db.session.query(clase_profesorModelo)
            page = 1
            per_page = 10
            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            clase_profesor = clase_profesor.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            clase_profesor_lista = [clase.to_json() for clase in clase_profesor.items]
            

            return {
                'Clase_Profesor': clase_profesor_lista,
                'Pagina': page,
                'Por pagina': per_page,
                'Total': clase_profesor.total
            }
        except Exception as e:
            return {'error': str(e)}, 404
        finally:
            db.session.close()
        
    # def post(self):
    #     # try:

    #         if request.args.get('profesor_id'):
    #             profesor_id = int(request.args.get('profesor_id'))
    #             # if profesor_id not in db.session.query(ProfesorModelo.idProfesor).all():
    #             #     abort(404, 'No se ha encontrado el Profesor')
            
    #         if request.args.get('clase_id'):
    #             clase_id = int(request.args.get('clase_id'))
    #             # if clase_id not in db.session.query(ClasesModelo.idClases).all():
    #             #     abort(404, 'No se ha encontrado la Clase')
            
    #         # clase_profesor_dic={}
    #         # clase_profesor_dic['profesor_id']=profesor_id
    #         # clase_profesor_dic['clase_id']=clase_id


    #         #     page = int(request.args.get('page'))
    #         # if request.args.get('per_page'):
    #         #     per_page = int(request.args.get('per_page'))
    #         # clase_profesor1 = clase_profesor.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
    #         # clase_profesor_nueva = clase_profesorModelo.from_json(request.get_json())
    #         # clase_profesor_nueva = profesor_id,clase_id
    #         #clase_profesor_nueva=clase_profesorModelo(profesor_id=profesor_id,clase_id=clase_id)
    #         clase_profesor_nueva=clase_profesorModelo(profesor_id=profesor_id,clase_id=clase_id)
    #         db.session.add(clase_profesor_nueva)
    #         db.session.commit()
    #         return clase_profesor_nueva.to_json(), 201
    #     # except BaseException:
    #     #     abort(404, 'Error al crear la Relacion: Clase_Profesor')
    #     # finally:
    #     #     db.session.close()

    def post(self):
        # try:
            campos_obligatorios = { 'profesor_id','clase_id'}
            datos = request.get_json()
            campos_recibidos = set(datos.keys())

            campos_faltantes = campos_obligatorios - campos_recibidos
            if campos_faltantes:
                raise Exception(f'Error al crear la rutina. Faltan campos obligatorios: {campos_faltantes}. Por favor, incluya estos campos y vuelva a intentarlo.')  # noqa

            for campo in campos_obligatorios:
                if datos[campo] is None:
                    raise Exception(f'Error al crear rutina. El campo {campo} no puede ser nulo. Por favor, proporcione un valor válido para {campo} y vuelva a intentarlo.')  # noqa:
            dato_nuevo = clase_profesorModelo.from_json(datos)
            db.session.add(dato_nuevo)
            db.session.commit()
            return dato_nuevo.to_json(), 201
        # except BaseException:
        #     abort(404, 'Error al crear la Relacion: Clase_Profesor')
        # finally:
        #     db.session.close()

class Clases_R(Resource):

    def get(self):
        try:
            clases = db.session.query(ClasesModelo)
            page = 1
            per_page = 10
            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            if request.args.get('idClases'):
                clases = clases.filter(ClasesModelo.idClases == int(request.args.get('idClases')))
            clases1 = clases.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            # clases_lista = list()
            # for clase in clases:
            #     clase_dict = {}
            #     clase_dict['idClases'] = clase.idClases
            #     clase_dict['nombre'] = clase.nombre
            #     clase_dict['dias'] = clase.dias
            #     clases_lista.append(clase_dict)
            clases_json = [clases.to_json() for clases in clases1.items]

            return {
                'Clases': clases_json,
                'Pagina': page,
                'Por pagina': per_page,
                'Total': clases1.total

            }
        except BaseException:
            abort(404, 'No se ha encontrado la Clase')
        finally:
            db.session.close()

    def post(self):
        try:
            clase_nueva = ClasesModelo.from_json(request.get_json())
            db.session.add(clase_nueva)
            db.session.commit()
            return clase_nueva.to_json(), 201
        except BaseException:
            abort(404, 'Error al crear la clase')
        finally:
            db.session.close()

    
    def delete(self):
        try:
            if request.args.get('idClases'):
                clases = db.session.query(ClasesModelo).get(request.args.get('idClases'))
                if clases:
                    pass
                else:
                    raise Exception(f"No se ha encontrado clases con la ID: {(request.args.get('idClases'))}")
                clase_eliminar = db.session.query(ClasesModelo).filter(ClasesModelo.idClases == request.args.get('idClases')).first()
                db.session.delete(clase_eliminar)
                db.session.commit()
                return 204, f"Clase con ID {request.args.get('idClases')} eliminado"
            else:
                raise Exception("El ID debe ser especificado para poder eliminar")
        except Exception:
            return {
                'error': str(Exception())
            }, 400
        finally:
            db.session.close()


    def put(self):

        try:
            if request.args.get('idClases'):
                registro = db.session.query(ClasesModelo).get(request.args.get('idClases'))
                if registro:
                    pass
                else:
                    raise Exception(f"No se ha encontrado la Clase con ID: {(request.args.get('idClases'))}")
                usuario_editar = db.session.query(ClasesModelo).filter(ClasesModelo.idClases == int(request.args.get('idClases'))).first()
                informacion = request.get_json().items()
                for campo, valor in informacion:                    
                    setattr(usuario_editar, campo, valor)
                db.session.add(usuario_editar)
                db.session.commit()
                return usuario_editar.to_json(), 201
            else:
                raise Exception('El ID de clases es necesario para actualizar')
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

class Clase_R(Resource):
    pass

#     # def delete(self, user_id):
#     #     try:
#     #         clase_eliminar = db.session.query(ClasesModelo).filter(
#     #             ClasesModelo.idClases == user_id).first()
#     #         db.session.delete(clase_eliminar)
#     #         db.session.commit()
#     #         return 204
#     #     except BaseException:
#     #         abort(404, 'No se ha encontrado la clase {}'.format(user_id))
#     #     finally:
#     #         db.session.close()

#     # def get(self, user_id):
#     #     try:
#     #         clase = db.session.query(ClasesModelo).filter(
#     #                ClasesModelo.idClases == user_id).first()
#     #         return clase.to_json(), 201
#     #     except BaseException:
#     #         abort(404, 'No se ha encontrado la Clase')
#     #     finally:
#     #         db.session.close()

#     def put(self, user_id):
#         try:
#             clase_modificar = db.session.query(ClasesModelo).filter(
#                 ClasesModelo.idClases == user_id).first()
#             informacion = request.get_json().items()
#             for campo, valor in informacion:
#                 setattr(clase_modificar, campo, valor)
#             db.session.add(clase_modificar)
#             db.session.commit()

#             return clase_modificar.to_json(), 201
#         except BaseException:
#             abort(404, 'No se ha encontrado la Clase')
#         finally:
#             db.session.close()
