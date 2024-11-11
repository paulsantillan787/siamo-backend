from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import PresupuestoRepuesto
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import presupuesto_respuesto_schema, presupuesto_respuesto_detail_schema

presupuesto_respuesto = Blueprint('presupuesto_respuesto', __name__)

# Se insertan varios repuestos en un presupuesto
@presupuesto_respuesto.route('/insert', methods=['POST'])
def insert_presupuesto_respuesto():
  data = request.get_json()
  id_presupuesto = data['id_presupuesto']
  # Lista de repuestos
  repuestos = data['repuestos']
  
  if not id_presupuesto or not repuestos:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  for repuesto in repuestos:
    new_presupuesto_respuesto = PresupuestoRepuesto(id_presupuesto, repuesto['id_repuesto'], repuesto['cantidad'])
    db.session.add(new_presupuesto_respuesto)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Presupuesto de repuestos creado'}), 201)

# Se filtran todos los registros con el mismo id_presupuesto
@presupuesto_respuesto.route('/get/<int:id_presupuesto>', methods=['GET'])
def get_presupuesto_respuesto(id_presupuesto):
  presupuesto_respuesto = PresupuestoRepuesto.query.filter_by(id_presupuesto=id_presupuesto).all()
  if not presupuesto_respuesto:
    return make_response(jsonify({'message': 'Presupuesto de repuestos no encontrado'}), 404)
  
  return make_response(jsonify(presupuesto_respuesto_detail_schema.dump(presupuesto_respuesto)), 200)