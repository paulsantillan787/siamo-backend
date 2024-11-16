from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Consulta
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import consulta_schema, consulta_detail_schema, consultas_detail_schema

consulta = Blueprint('consulta', __name__)

@consulta.route('/insert', methods=['POST'])
def insert_consulta():
  data = request.get_json()
  prob_declarado = data['prob_declarado']
  estado = data['estado']
  id_cliente = data['id_cliente']
  id_tecnico = data['id_tecnico']
  id_automovil = data['id_automovil']
  
  if not prob_declarado or not estado or not id_cliente or not id_tecnico or not id_automovil:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  new_consulta = Consulta(prob_declarado, estado, id_cliente, id_tecnico, id_automovil)
  db.session.add(new_consulta)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Consulta creada', 'id': new_consulta.id_consulta}), 201)

@consulta.route('/get/<int:id>', methods=['GET'])
def get_consulta(id):
  consulta = Consulta.query.filter_by(id_consulta=id).first()
  if not consulta:
    return make_response(jsonify({'message': 'Consulta no encontrada'}), 404)
  
  return make_response(jsonify(consulta_schema.dump(consulta)), 200)

@consulta.route('/get/details/<int:id>', methods=['GET'])
def get_consulta_details(id):
  consulta = Consulta.query.filter_by(id_consulta=id).first()
  if not consulta:
    return make_response(jsonify({'message': 'Consulta no encontrada'}), 404)
  
  return make_response(jsonify(consulta_detail_schema.dump(consulta)), 200)

@consulta.route('/get/all', methods=['GET'])
def get_all_consultas():
  consultas = Consulta.query.all()
  return make_response(jsonify(consultas_detail_schema.dump(consultas, many=True)), 200)