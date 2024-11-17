from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Tecnico
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import tecnico_schema, tecnico_detail_schema, tecnicos_schema

tecnico = Blueprint('tecnico', __name__)

@tecnico.route('/insert', methods=['POST'])
def insert_tecnico():
  data = request.get_json()
  id_empleado = data['id_empleado']
  
  if not id_empleado:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  tecnico = Tecnico.query.filter_by(id_empleado=id_empleado).first()
  if tecnico:
    return make_response(jsonify({'message': 'El tecnico ya existe'}), 400)
  
  new_tecnico = Tecnico(id_empleado)
  db.session.add(new_tecnico)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Tecnico creado', 'id': new_tecnico.id_tecnico}), 201)

@tecnico.route('/get/<int:id>', methods=['GET'])
def get_tecnico(id):
  tecnico = Tecnico.query.filter_by(id_tecnico=id).first()
  if not tecnico:
    return make_response(jsonify({'message': 'Tecnico no encontrado'}), 404)
  
  return make_response(jsonify(tecnico_schema.dump(tecnico)), 200)

@tecnico.route('/get/details/<int:id>', methods=['GET'])
def get_tecnico_details(id):
  tecnico = Tecnico.query.filter_by(id_tecnico=id).first()
  if not tecnico:
    return make_response(jsonify({'message': 'Tecnico no encontrado'}), 404)
  
  return make_response(jsonify(tecnico_detail_schema.dump(tecnico)), 200)

@tecnico.route('/get/all', methods=['GET'])
def get_all_tecnicos():
  tecnicos = Tecnico.query.all()
  if not tecnicos:
    return make_response(jsonify({'message': 'No hay tecnicos'}), 404)
        
  return make_response(jsonify(tecnicos_schema.dump(tecnicos)), 200)