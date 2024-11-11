from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Problema
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import problema_schema, problema_detail_schema, problemas_detail_schema

problema = Blueprint('problema', __name__)

@problema.route('/insert', methods=['POST'])
def insert_problema():
  data = request.get_json()
  descripcion = data['descripcion']
  detalle = data['detalle']
  id_solucion = data['id_solucion']
  
  if not descripcion or not detalle or not id_solucion:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  new_problema = Problema(descripcion, detalle, id_solucion)
  db.session.add(new_problema)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Problema creado', 'id': new_problema.id_problema}), 201)

@problema.route('/get/<int:id>', methods=['GET'])
def get_problema(id):
  problema = Problema.query.filter_by(id_problema=id).first()
  if not problema:
    return make_response(jsonify({'message': 'Problema no encontrado'}), 404)
  
  return make_response(jsonify(problema_schema.dump(problema)), 200)

@problema.route('/get/details/<int:id>', methods=['GET'])
def get_problema_details(id):
  problema = Problema.query.filter_by(id_problema=id).first()
  if not problema:
    return make_response(jsonify({'message': 'Problema no encontrado'}), 404)
  
  return make_response(jsonify(problema_detail_schema.dump(problema)), 200)

@problema.route('/get/all', methods=['GET'])
def get_problemas():
  problemas = Problema.query.all()
  if not problemas:
    return make_response(jsonify({'message': 'No hay problemas'}), 404)
  
  return make_response(jsonify(problemas_detail_schema.dump(problemas)), 200)