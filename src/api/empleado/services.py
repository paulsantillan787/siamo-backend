from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from src.api.persona.models import Persona
from .models import Empleado
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import empleado_schema, empleado_detail_schema, empleado_login_schema
from src.api.recepcionista.models import Recepcionista
from src.api.tecnico.models import Tecnico

empleado = Blueprint('empleado', __name__)

@empleado.route('/insert', methods=['POST'])
def insert_empleado():
  data = request.get_json()
  fecha_ingreso = data['fecha_ingreso']
  cod_empleado = data['cod_empleado']
  contrasenia = data['contrasenia']
  id_persona = data['id_persona']
  
  if not fecha_ingreso or not cod_empleado or not contrasenia or not id_persona:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  persona = Persona.query.filter_by(id_persona=id_persona).first()
  if not persona:
    return make_response(jsonify({'message': 'La persona no existe'}), 400)
  
  empleado = Empleado.query.filter_by(cod_empleado=cod_empleado).first()
  if empleado:
    return make_response(jsonify({'message': 'El empleado ya existe'}), 400)
  
  new_empleado = Empleado(fecha_ingreso, cod_empleado, contrasenia, id_persona)
  db.session.add(new_empleado)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Empleado creado', 'id': new_empleado.id_empleado}), 201)

@empleado.route('/get/<int:id>', methods=['GET'])
def get_empleado(id):
  empleado = Empleado.query.filter_by(id_empleado=id).first()
  if not empleado:
    return make_response(jsonify({'message': 'Empleado no encontrado'}), 404)
  
  return make_response(jsonify(empleado_schema.dump(empleado)), 200)

@empleado.route('/get/details/<int:id>', methods=['GET'])
def get_empleado_details(id):
  empleado = Empleado.query.filter_by(id_empleado=id).first()
  if not empleado:
    return make_response(jsonify({'message': 'Empleado no encontrado'}), 404)
  
  return make_response(jsonify(empleado_detail_schema.dump(empleado)), 200)

@empleado.route('/login/<int:codEmpleado>/<string:contrasenia>', methods=['GET'])
def login_empleado(codEmpleado, contrasenia):
  empleado = Empleado.query.filter_by(cod_empleado=codEmpleado, contrasenia=contrasenia).first()
  if not empleado:
    return make_response(jsonify({'message': 'Empleado no encontrado'}), 404)
  
  empleado_data = empleado_login_schema.dump(empleado)
  if Recepcionista.query.filter_by(id_empleado=empleado.id_empleado).first():
    empleado_data['tipo_empleado'] = 1
  elif Tecnico.query.filter_by(id_empleado=empleado.id_empleado).first():
    empleado_data['tipo_empleado'] = 2
    empleado_data['id_tecnico'] = Tecnico.query.filter_by(id_empleado=empleado.id_empleado).first().id_tecnico
  else:
    return make_response(jsonify({'message': 'Empleado no encontrado'}), 404)
  
  return make_response(jsonify(empleado_data), 200)
  