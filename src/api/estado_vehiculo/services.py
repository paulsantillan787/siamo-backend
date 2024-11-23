from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import EstadoVehiculo
from .schema import estado_vehiculo_schema
from src.common.utils.db import db
from src.common.utils.data import data

estado_vehiculo = Blueprint('estado_vehiculo', __name__)

@estado_vehiculo.route('/insert', methods=['POST'])
def insert_estado_vehiculo():
  data = request.get_json()
  estado_carroceria = data['estado_carroceria']
  estado_neumaticos = data['estado_neumaticos']
  estado_motor = data['estado_motor']
  estado_frenos = data['estado_frenos']
  id_ficha_ingreso = data['id_ficha_ingreso']
  
  if not estado_carroceria or not estado_neumaticos or not estado_motor or not estado_frenos or not id_ficha_ingreso:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  new_estado_vehiculo = EstadoVehiculo(estado_carroceria, estado_neumaticos, estado_motor, estado_frenos, id_ficha_ingreso)
  db.session.add(new_estado_vehiculo)
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Estado de vehículo creado', 'id': new_estado_vehiculo.id_estado_vehiculo}), 201)


@estado_vehiculo.route('/get/<int:id_ficha_ingreso>', methods=['GET'])
def get_estado_vehiculo_by_ficha_ingreso(id_ficha_ingreso):
  estado_vehiculo = EstadoVehiculo.query.filter_by(id_ficha_ingreso=id_ficha_ingreso).first()
  if not estado_vehiculo:
    return make_response(jsonify({'mensaje': 'Estado de vehículo no encontrado'}), 404)
  
  return make_response(jsonify(estado_vehiculo_schema.dump(estado_vehiculo)), 200)

