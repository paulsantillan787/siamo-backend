from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Solucion
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import solucion_schema

solucion = Blueprint('solucion', __name__)

@solucion.route('/insert', methods=['POST'])
def insert_solucion():
  data = request.get_json()
  descripcion = data['descripcion']
  
  if not descripcion:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  solucion = Solucion.query.filter_by(descripcion=descripcion).first()
  if solucion:
    return make_response(jsonify({'message': 'La solucion ya existe'}), 400)
  
  new_solucion = Solucion(descripcion)
  db.session.add(new_solucion)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Solucion creada', 'id': new_solucion.id_solucion}), 201)

@solucion.route('/get/<int:id>', methods=['GET'])
def get_solucion(id):
  solucion = Solucion.query.filter_by(id_solucion=id).first()
  if not solucion:
    return make_response(jsonify({'message': 'Solucion no encontrada'}), 404)
  
  return make_response(jsonify(solucion_schema.dump(solucion)), 200)