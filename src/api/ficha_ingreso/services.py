from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import FichaIngreso
from .schema import ficha_ingreso_schema
from src.common.utils.db import db
from src.common.utils.data import data

ficha_ingreso = Blueprint('ficha_ingreso', __name__)

@ficha_ingreso.route('/insert', methods=['POST'])
def insert_ficha_ingreso():
  data = request.get_json()
  fecha_aprox_recojo = data['fecha_aprox_recojo']
  id_ost = data['id_ost']
  
  if not fecha_aprox_recojo or not id_ost:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  new_ficha_ingreso = FichaIngreso(fecha_aprox_recojo, id_ost)
  db.session.add(new_ficha_ingreso)
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Ficha de ingreso creada', 'id': new_ficha_ingreso.id_ficha_ingreso}), 201)

@ficha_ingreso.route('/get/<int:id_ost>', methods=['GET'])
def get_ficha_ingreso_by_ost(id_ost):
  ficha_ingreso = FichaIngreso.query.filter_by(id_ost=id_ost).first()
  if not ficha_ingreso:
    return make_response(jsonify({'mensaje': 'Ficha de ingreso no encontrada'}), 404)
  
  return make_response(jsonify(ficha_ingreso_schema.dump(ficha_ingreso)), 200)