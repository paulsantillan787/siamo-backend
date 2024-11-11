from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from src.api.persona.models import Persona
from .models import Cliente
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import cliente_schema, cliente_detail_schema

cliente = Blueprint('cliente', __name__)

@cliente.route('/insert', methods=['POST'])
def insert_cliente():
  data = request.get_json()
  id_persona = data['id_persona']
  
  if not id_persona:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  persona = Persona.query.filter_by(id_persona=id_persona).first()
  if not persona:
    return make_response(jsonify({'message': 'La persona no existe'}), 400)
  
  new_cliente = Cliente(id_persona)
  db.session.add(new_cliente)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Cliente creado', 'id': new_cliente.id_cliente}), 201)

@cliente.route('/get/<int:id>', methods=['GET'])
def get_cliente(id):
  cliente = Cliente.query.filter_by(id_cliente=id).first()
  if not cliente:
    return make_response(jsonify({'message': 'Cliente no encontrado'}), 404)
  
  return make_response(jsonify(cliente_schema.dump(cliente)), 200)

@cliente.route('/get/details/<int:id>', methods=['GET'])
def get_cliente_details(id):
  cliente = Cliente.query.filter_by(id_cliente=id).first()
  if not cliente:
    return make_response(jsonify({'message': 'Cliente no encontrado'}), 404)
  
  return make_response(jsonify(cliente_detail_schema.dump(cliente)), 200)

@cliente.route('/get/doc/<string:num_doc>', methods=['GET'])
def get_cliente_doc(num_doc):
  persona = Persona.query.filter_by(num_doc=num_doc).first()
  if not persona:
    return make_response(jsonify({'message': 'Persona no encontrado'}), 404)
  cliente = Cliente.query.filter_by(id_persona=persona.id_persona).first()
  if not cliente:
    return make_response(jsonify({'message': 'Cliente no encontrado'}), 404)
  
  return make_response(jsonify(cliente_detail_schema.dump(cliente)), 200)