from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from src.api.cliente.models import Cliente
from .models import Automovil
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import automovil_schema, automovil_detail_schema

automovil = Blueprint('automovil', __name__)

@automovil.route('/insert', methods=['POST'])
def insert_automovil():
  data = request.get_json()
  placa = data['placa']
  marca = data['marca']
  modelo = data['modelo']
  id_cliente = data['id_cliente']
  
  if not placa or not marca or not modelo or not id_cliente:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  cliente = Cliente.query.filter_by(id_cliente=id_cliente).first()
  if not cliente:
    return make_response(jsonify({'message': 'El cliente no existe'}), 400)
  
  automovil = Automovil.query.filter_by(placa=placa).first()
  if automovil:
    return make_response(jsonify({'message': 'El automovil ya existe'}), 400)
  
  new_automovil = Automovil(placa, marca, modelo, id_cliente)
  db.session.add(new_automovil)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Automovil creado', 'id': new_automovil.id_automovil}), 201)

@automovil.route('/get/<int:id>/<string:placa>', methods=['GET'])
def get_automovil_placa_cliente(id, placa):
  automovil = Automovil.query.filter_by(id_cliente=id, placa=placa).first()
  if not automovil:
    return make_response(jsonify({'message': 'Automovil no encontrado'}), 404)
  
  return make_response(jsonify(automovil_schema.dump(automovil)), 200)

@automovil.route('/get/details/<string:placa>', methods=['GET'])
def get_automovil_details(placa):
  automovil = Automovil.query.filter_by(placa=placa).first()
  if not automovil:
    return make_response(jsonify({'message': 'Automovil no encontrado'}), 404)
  
  return make_response(jsonify(automovil_detail_schema.dump(automovil)), 200)