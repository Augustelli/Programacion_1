from flask_restful import Resource
from flask import abort, request, jsonify
from main.models import PagosModelo, UsuarioModelo
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity  # noqa
from main.auth.decorators import role_required
from datetime import datetime


class Pago(Resource):

  
    @role_required(roles=['admin', 'profesor'])
    def put(self):
        try:
            if request.args.get('nrDni'):
                pago = db.session.query(PagosModelo).filter(PagosModelo.dni == (request.args.get('nrDni'))).order_by(PagosModelo.estado.asc()).all()  # noqa
                pago.estado = "No pagado" if pago.estado == "Pagado" else "Pagado"
                usuario = db.session.query(UsuarioModelo).filter_by(UsuarioModelo.dni == (request.args.get('nrDni'))).first()
                usuario.estado = pago.estado
                db.session.commit()
                return pago.to_json(), 201
            else:
                raise Exception('Debe indicarse número de DNI para poder modificar el pago.')
        except Exception:
            abort(404, f"No se pudo realizar la actualización del estado. Usuario id {(request.args.get('nrDni'))}")
        finally:
            db.session.close()

    @role_required(roles=['admin', 'profesor'])
    def delete(self):
        try:
            if request.args.get('idPago'):
                pago_eliminar = db.session.query(PagosModelo).filter(PagosModelo.idPago == (request.args.get('idPago'))).first()
                db.session.delete(pago_eliminar)
                db.session.commit()
                return 204
        except BaseException:
            abort(404, 'No se ha encontrado el pago  {}'.format((request.args.get('idPago'))))
        finally:
            db.session.close()


class Pagos(Resource):
    @role_required(roles=['admin', 'profesor', 'alumno'])
    def post(self):
        try:
            dato_nuevo = PagosModelo.from_json(request.get_json())
            db.session.add(dato_nuevo)
            db.session.commit()
            return dato_nuevo.to_json(), 201
        except BaseException:
            abort(404, 'Error al crear el Pago')
        finally:
            db.session.close()

            
    @role_required(roles=['admin', 'profesor'])
    def get(self):
        try:

            pagos = db.session.query(PagosModelo)

            if request.args.get('nrDni'):

                pagos = pagos.filter(PagosModelo.dni == request.args.get('nrDni')).order_by(PagosModelo.fecha_de_pago.desc())
            page = 1
            per_page = 10
            if request.args.get('page'):
                page = (request.args.get('page'))
            if request.args.get('per_page'):
                per_page = (request.args.get('per_page'))
            pagos = pagos.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30)
            pagos_json = [pago.to_json() for pago in pagos]
            return jsonify({'Pagos': pagos_json,
                            'Pagina': page,
                            'Por pagina': per_page,
                            'Total': pagos.total})
        except Exception:
            abort(404, 'No se ha podido realizar la consulta')
        finally:
            db.session.close()

   
    def put(self):
        try:
            idPago = request.args.get('idPago')
            if idPago:
                registro = db.session.query(PagosModelo).get(idPago)
                if registro:
                    informacion = request.get_json()
                    for campo, valor in informacion.items():
                        if campo == 'fecha_de_pago':
                        
                            fecha_procesada = datetime.strptime(valor, "%d/%m/%Y")
                            setattr(registro, campo, fecha_procesada)
                            print(f"Se ha actualizado el campo {campo} con el valor {fecha_procesada}.")
                        elif hasattr(registro, campo):
                            setattr(registro, campo, valor)
                            print(f"Se ha actualizado el campo {campo} con el valor {valor}.")
                        else:

                            raise Exception(f"El campo {campo} no es válido para la actualización.")
                    db.session.commit()
                    return registro.to_json(), 201
                else:
                    return {'error': f"No se ha encontrado usuario con idPago: {idPago}"}, 404
            else:
                return {'error': 'El idPago del usuario es necesario para poder modificarlo.'}, 400
        except Exception as e:
            return {'error': str(e)}, 400
        finally:
            db.session.close()

