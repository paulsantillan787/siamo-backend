from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import OrdenServicioTecnico
from src.api.ficha_ingreso.models import FichaIngreso
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import ost_menu_schema, lista_ost_menu_schema, ost_schema

ost = Blueprint('ost', __name__)

@ost.route('/insert', methods=['POST'])
def insert_ost():
  data = request.get_json()
  id_consulta = data['id_consulta']
  fecha_aprox_ingreso = data['fecha_aprox_ingreso']
  
  if not id_consulta or not fecha_aprox_ingreso:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  new_ost = OrdenServicioTecnico(id_consulta, fecha_aprox_ingreso)
  db.session.add(new_ost)
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Orden de servicio técnico creada', 'id': new_ost.id_ost}), 201)

@ost.route('/get/<int:id>', methods=['GET'])
def get_ost(id):
  ost = OrdenServicioTecnico.query.filter_by(id_ost=id).first()
  if not ost:
    return make_response(jsonify({'mensaje': 'Orden de servicio técnico no encontrada'}), 404)
  
  return make_response(jsonify(ost_schema.dump(ost)), 200)

@ost.route('/get_all_menu', methods=['GET'])
def get_all_ost_menu():
  osts = OrdenServicioTecnico.query.all()
  osts = OrdenServicioTecnico.query.filter(
      OrdenServicioTecnico.id_ost.in_(
          db.session.query(FichaIngreso.id_ost).distinct()
      ),
      OrdenServicioTecnico.estado == 1
  ).all()
  if not osts:
    return make_response(jsonify({'mensaje': 'Ordenes de servicio técnico no encontradas'}), 404)
  
  return make_response(jsonify(lista_ost_menu_schema.dump(osts)), 200)

@ost.route('/update/<int:id>', methods=['PUT'])
def update_estado_ost(id):
  data = request.get_json()
  estado = data['estado']
  
  if not estado:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  ost = OrdenServicioTecnico.query.filter_by(id_ost=id).first()
  if not ost:
    return make_response(jsonify({'mensaje': 'Orden de servicio técnico no encontrada'}), 404)
  
  ost.estado = estado
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Estado de orden de servicio técnico actualizado'}), 200)


