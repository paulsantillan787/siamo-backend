from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import ListaTareas
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import lista_tareas_schema

lista_tareas = Blueprint('lista_tareas', __name__)

@lista_tareas.route('/insert', methods=['POST'])
def insert_lista_tareas():
  data = request.get_json()
  id_ost = data['id_ost']
  
  if not id_ost:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  new_lista_tareas = ListaTareas(id_ost)
  db.session.add(new_lista_tareas)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Lista de tareas creada', 'id': new_lista_tareas.id_lista_tareas}), 201)

@lista_tareas.route('/get/<int:id_ost>', methods=['GET'])
def get_lista_tareas(id_ost):
  lista_tareas = ListaTareas.query.filter_by(id_ost=id_ost).first()
  if not lista_tareas:
    return make_response(jsonify({'message': 'Lista de tareas no encontrada'}), 404)
  
  return make_response(jsonify(lista_tareas_schema.dump(lista_tareas)), 200)