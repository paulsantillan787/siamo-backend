from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Presupuesto
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import presupuesto_schema

presupuesto = Blueprint('presupuesto', __name__)

@presupuesto.route('/insert', methods=['POST'])
def insert_presupuesto():
  data = request.get_json()
  tarifa_mano_obra = data['tarifa_mano_obra']
  tarifa_repuestos = data['tarifa_repuestos']
  descuento_negociado = data['descuento_negociado']
  id_consulta = data['id_consulta']
  
  if not tarifa_mano_obra or not tarifa_repuestos or not descuento_negociado or not id_consulta:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  new_presupuesto = Presupuesto(tarifa_mano_obra, tarifa_repuestos, descuento_negociado, id_consulta)
  db.session.add(new_presupuesto)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Presupuesto creado'}), 201)

@presupuesto.route('/get/<int:id_consulta>', methods=['GET'])
def get_presupuesto(id_consulta):
  presupuesto = Presupuesto.query.filter_by(id_consulta=id_consulta).first()
  if not presupuesto:
    return make_response(jsonify({'message': 'Presupuesto no encontrado'}), 404)
  
  return make_response(jsonify(presupuesto_schema.dump(presupuesto)), 200)