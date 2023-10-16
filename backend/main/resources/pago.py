from flask_restful import Resource
from flask import abort, request, jsonify
from main.models import PagosModelo, UsuarioModelo
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity  # noqa
from main.auth.decorators import role_required


class Pago(Resource):

    # def get(self, (request.args.get('nrDni'))):
    #     try:
    #         rescate_pago = db.session.query(PagosModelo).filter(
    #             PagosModelo.idPago == (request.args.get('nrDni'))
    #         ).first()

    #         return rescate_pago.to_json(), 201

    #     except BaseException:
    #         abort(404, 'No se ha encontrado pagos del alumnmo')

    #     finally:
    #         db.session.close()

    #   def get(self, (request.args.get('nrDni'))):
    # try:
    #     usuario_rescatado = db.session.query(UsuarioModelo).filter(
    #         UsuarioModelo.dni == (request.args.get('nrDni'))).first()
    #     return usuario_rescatado.to_json(), 201
    # except Exception:
    #     abort(404, f'No se ha encontrado del usuario de id: {(request.args.get('nrDni'))}')
    # finally:
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
            if request.args.get('idPago'):
                registro = db.session.query(PagosModelo).get(request.args.get('idPago'))
                if registro:
                    pass
                else:
                    raise Exception(f"No se ha encontrado usuario con DNI: {(request.args.get('idPago'))}")
                usuario_editar = db.session.query(PagosModelo).filter(PagosModelo.idPago == (request.args.get('idPago'))).first()
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
