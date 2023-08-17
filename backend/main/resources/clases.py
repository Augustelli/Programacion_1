from flask import request, abort, jsonify
from .. import db
from main.models import ClasesModelo, clase_profesorModelo, ProfesorModelo
from flask_restful import Resource
from main.auth.decorators import role_required
from sqlalchemy import desc


class Clase_Profesor_R(Resource):

    def get(self):
        if request.args.get('idClase'):
            clase = db.session.query(ClasesModelo)
            profesor = db.session.query(ProfesorModelo)
            clase_profesor = clase.outerjoin(clase_profesorModelo).filter(request.args.get('idClase') == clase_profesorModelo.idClase)

            # clase_profesor = clase.outerjoin(clase_profesorModelo).filter(request.args.get('idClase') == clase_profesorModelo.clase_id)
            clase_profesor = clase_profesor.outerjoin(profesor).filter(clase_profesorModelo.profesor_id == profesor.idProfesor)
            clase_profesor_lista = [clase.to_json() for clase in clase_profesor.items]
            return jsonify(clase_profesor_lista)
        if request.args.get('idProfesor'):
            clase = db.session.query(ClasesModelo)
            profesor = db.session.query(ProfesorModelo)
            clase_profesor = clase.outerjoin(clase_profesorModelo).filter(request.args.get('idProfesor') == clase_profesorModelo.profesor_id)
            clase_profesor = clase_profesor.outerjoin(profesor).filter(clase_profesorModelo.clase_id == profesor.idProfesor)
            clase_profesor_lista = [clase.to_json() for clase in clase_profesor.items]
            return jsonify(clase_profesor_lista)
    # def get(self):
    #     #try:
    #         clase_profesor = db.session.query(clase_profesorModelo)
    #         # page = 1
    #         # per_page = 10
    #         # if request.args.get('page'):
    #         #     page = int(request.args.get('page'))
    #         # if request.args.get('per_page'):
    #         #     per_page = int(request.args.get('per_page'))
    #         # clase_profesor = clase_profesor.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
    #         # clase_profesor_lista = [clase.to_json() for clase in clase_profesor.items]

    #         if request.args.get('idClase'):
    #                 clase = db.session.query(ClasesModelo)
    #                 profesor = db.session.query(ProfesorModelo)
    #                 clase_profesor = clase.outerjoin(clase_profesor).filter(request.args.get('idClase') == clase_profesor.clase_id)
    #                 clase_profesor = clase_profesor.outerjoin(profesor).filter(clase_profesor.profesor_id == profesor.idProfesor)
    #                 resultados = clase_profesor.all()

    #                 profesor_data = []

    #                 for resultado in resultados:
    #                     data = {

    #                         'idClases': resultado.idClases,
    #                         'nombre': resultado.nombre,
    #                         'dias': resultado.dias,
    #                         'idProfesor': resultado.profesor.idProfesor,
    #                         'profesor_dni': resultado.profesor.profesor_dni,
    #                         'especialidad': self.profesor.especialidad
    #                     }
    #                     profesor_data.append(data)

    #                 # Imprimir la información
    #                 return jsonify(profesor_data)
    #     #     return {
    #     #         'Clase_Profesor': clase_profesor_lista,
    #     #         'Pagina': page,
    #     #         'Por pagina': per_page,
    #     #         'Total': clase_profesor.total
    #     #     }
    #     # except Exception as e:
    #     #     return {'error': str(e)}, 404
    #     # finally:
    #     #     db.session.close()

# # db.session.close()

    # def get(self):
            
    #     # try:
    #         if request.args.get('idClase') or request.args.get('idProfesor'):
    #             claseq = db.session.query(ClasesModelo)
    #             Profesor = db.session.query(ProfesorModelo)
    #             clase_profesor = db.session.query(clase_profesorModelo).filter_by(clase_id=request.args.get('idClase'), profesor_id=request.args.get('idProfesor')).first()
    #             
                # clase_profesor = db.session.query(clase_profesorModelo)
                # clase_profesorClase = clase_profesor.filter_by(clase_profesor.clase_id == request.arg.get('idClase'))
                # clase_profesorProfesor = clase_profesor.filter_by(clase_profesor.profesor_id == request.arg.get('idProfesor'))
                
    #             resultado = {
    #                 'idClases': claseq.idClases,
    #                 'nombre': claseq.nombre,
    #                 'dias': claseq.dias,
    #                 'idProfesor': profesorq.idProfesor,
    #                 'profesor_dni': profesorq.profesor_dni,
    #                 'especialidad': profesorq.especialidad
                # }


    @role_required(roles=['admin', 'profesor'])
    def post(self):
        try:
                data = request.get_json()
                check = 0
           
                for campo, valor in data.items():
                    if campo == 'idClase':
                        id_clase = int(valor)
                        check += 1
                    
                    if campo == 'idProfesor':
                        id_profesor = int(valor)
                        check += 1
                    
                if check == 2:
                    clase = db.session.query(ClasesModelo).filter_by(idClases=id_clase).first()
                    profesor = db.session.query(ProfesorModelo).filter_by(idProfesor=id_profesor).first()

                    if clase is not None and profesor is not None:
                        clase.profesores.append(profesor)
                        db.session.commit()

                        return {'message': 'Profesor agregado a la clase exitosamente.'}, 201
                else:
                    return {'error': 'Dato de Profesor o Clase no encontrados'}, 404
               
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
 
    @role_required(roles=['admin', 'profesor'])
    def delete(self):
        try:           
            data = request.get_json()
            print(data)
            check = 0
                            
            for campo, valor in data.items():
                if campo == 'idClase':
                    id_clase = int(valor)
                    check += 1
                if campo == 'idProfesor':
                    id_profesor = int(valor)
                    check += 1
            
            if check == 2:
                clase = db.session.query(ClasesModelo).filter_by(idClases=id_clase).first()
                profesor = db.session.query(ProfesorModelo).filter_by(idProfesor=id_profesor).first()

                if clase is not None and profesor is not None:
                    clase.profesores.remove(profesor)
                    db.session.commit()

                    return {'message': 'Profesor eliminado a la clase exitosamente.'}, 201
            else:
                return {'error': 'Falta un dato para su eliminación'}, 404
               
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
 

class Clases_R(Resource):
    
    @role_required(roles=['admin', 'profesor'])
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

    @role_required(roles=['admin', 'profesor'])
    def post(self):
        try:
            datos = request.get_json()
            clase_nueva = ClasesModelo.from_json(request.get_json())
            db.session.add(clase_nueva)
            db.session.commit()
            if 'idProfesor' in datos:
                    id_profesor = datos['idProfesor']
                    print(id_profesor)
                    id_clase = db.session.query(ClasesModelo).order_by(desc(ClasesModelo.idClases)).first().idClases
                    print(id_clase)
                    try:
                        profesor = db.session.query(ProfesorModelo).filter_by(idProfesor=id_profesor).first()
                        clase = db.session.query(ClasesModelo).filter_by(idClases=id_clase).first()
                        clase.profesores.append(profesor)
                        db.session.commit()
                    except Exception as e:
                        return {'error': 'No existe ese profesor'}, 400
            return clase_nueva.to_json(), 201
        except BaseException:
            abort(404, 'Error al crear la clase')
        finally:
            db.session.close()

    @role_required(roles=['admin', 'profesor'])
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

    @role_required(roles=['admin', 'profesor'])
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
# #     # def delete(self, user_id):
# #     #     try:
# #     #         clase_eliminar = db.session.query(ClasesModelo).filter(
# #     #             ClasesModelo.idClases == user_id).first()
# #     #         db.session.delete(clase_eliminar)
# #     #         db.session.commit()
# #     #         return 204
# #     #     except BaseException:
# #     #         abort(404, 'No se ha encontrado la clase {}'.format(user_id))
# #     #     finally:
# #     #         db.session.close()

# #     # def get(self, user_id):
# #     #     try:
# #     #         clase = db.session.query(ClasesModelo).filter(
# #     #                ClasesModelo.idClases == user_id).first()
# #     #         return clase.to_json(), 201
# #     #     except BaseException:
# #     #         abort(404, 'No se ha encontrado la Clase')
# #     #     finally:
# #     #         db.session.close()

# #     def put(self, user_id):
# #         try:
# #             clase_modificar = db.session.query(ClasesModelo).filter(
# #                 ClasesModelo.idClases == user_id).first()
# #             informacion = request.get_json().items()
# #             for campo, valor in informacion:
# #                 setattr(clase_modificar, campo, valor)
# #             db.session.add(clase_modificar)
# #             db.session.commit()

# #             return clase_modificar.to_json(), 201
# #         except BaseException:
# #             abort(404, 'No se ha encontrado la Clase')
# #         finally:
