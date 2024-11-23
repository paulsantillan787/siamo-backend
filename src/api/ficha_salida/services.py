from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import FichaSalida
from .schema import ficha_salida_schema
from src.common.utils.db import db
from src.common.utils.data import data

ficha_salida = Blueprint('ficha_salida', __name__)

@ficha_salida.route('/insert', methods=['POST'])
def insert_ficha_salida():
  data = request.get_json()
  id_ost = data['id_ost']
  
  if not id_ost:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  new_ficha_salida = FichaSalida(id_ost)
  db.session.add(new_ficha_salida)
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Ficha de salida creada', 'id': new_ficha_salida.id_ficha_salida}), 201)

@ficha_salida.route('/get/<int:id_ost>', methods=['GET'])
def get_ficha_salida_by_ost(id_ost):
  ficha_salida = FichaSalida.query.filter_by(id_ost=id_ost).first()
  if not ficha_salida:
    return make_response(jsonify({'mensaje': 'Ficha de salida no encontrada'}), 404)
  
  return make_response(jsonify(ficha_salida_schema.dump(ficha_salida)), 200)