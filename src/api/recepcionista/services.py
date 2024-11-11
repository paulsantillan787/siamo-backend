from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Recepcionista
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import recepcionista_schema, recepcionista_detail_schema

recepcionista = Blueprint('recepcionista', __name__)

@recepcionista.route('/insert', methods=['POST'])
def insert_recepcionista():
  data = request.get_json()
  id_empleado = data['id_empleado']
  
  if not id_empleado:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  recepcionista = Recepcionista.query.filter_by(id_empleado=id_empleado).first()
  if recepcionista:
    return make_response(jsonify({'message': 'El recepcionista ya existe'}), 400)
  
  new_recepcionista = Recepcionista(id_empleado)
  db.session.add(new_recepcionista)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Recepcionista creado', 'id': new_recepcionista.id_recepcionista}), 201)

@recepcionista.route('/get/<int:id>', methods=['GET'])
def get_recepcionista(id):
  recepcionista = Recepcionista.query.filter_by(id_recepcionista=id).first()
  if not recepcionista:
    return make_response(jsonify({'message': 'Recepcionista no encontrado'}), 404)
  
  return make_response(jsonify(recepcionista_schema.dump(recepcionista)), 200)

@recepcionista.route('/get/details/<int:id>', methods=['GET'])
def get_recepcionista_details(id):
  recepcionista = Recepcionista.query.filter_by(id_recepcionista=id).first()
  if not recepcionista:
    return make_response(jsonify({'message': 'Recepcionista no encontrado'}), 404)
  
  return make_response(jsonify(recepcionista_detail_schema.dump(recepcionista)), 200)