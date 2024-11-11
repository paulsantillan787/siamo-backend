from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Repuesto
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import repuesto_schema, repuestos_schema

repuesto = Blueprint('repuesto', __name__)

@repuesto.route('/insert', methods=['POST'])
def insert_repuesto():
  data = request.get_json()
  descripcion = data['descripcion']
  precio = data['precio']
  
  if not descripcion or not precio:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)

  try:
        precio = float(precio)
  except ValueError:
      return make_response(jsonify({'message': 'El precio debe ser un número'}), 400)
  
  new_repuesto = Repuesto(descripcion, precio)
  db.session.add(new_repuesto)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Repuesto creado', 'id': new_repuesto.id_repuesto}), 201)

@repuesto.route('/get/<int:id>', methods=['GET'])
def get_repuesto(id):
  repuesto = Repuesto.query.filter_by(id_repuesto=id).first()
  if not repuesto:
    return make_response(jsonify({'message': 'Repuesto no encontrado'}), 404)
  
  return make_response(jsonify(repuesto_schema.dump(repuesto)), 200)

@repuesto.route('/get/all', methods=['GET'])
def get_repuestos():
  repuestos = Repuesto.query.all()
  if not repuestos:
    return make_response(jsonify({'message': 'No hay repuestos'}), 404)
  
  return make_response(jsonify(repuestos_schema.dump(repuestos)), 200)