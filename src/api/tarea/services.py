from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Tarea
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import tareas_schema, lista_tareas_schema

tarea = Blueprint('tarea', __name__)

@tarea.route('/insert', methods=['POST'])
def insert_tarea():
  data = request.get_json()
  descripcion = data['descripcion']
  id_lista_tareas = data['id_lista_tareas']
  id_tecnico = data['id_tecnico']
  
  if not descripcion or not id_tecnico or not id_lista_tareas:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  new_tarea = Tarea(descripcion, id_lista_tareas, id_tecnico)
  db.session.add(new_tarea)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Tarea creada', 'id': new_tarea.id_tarea}), 201)

@tarea.route('/get/<int:id_lista_tareas>', methods=['GET'])
def get_lista_tareas(id_lista_tareas):
  tareas = Tarea.query.filter_by(id_lista_tareas=id_lista_tareas).all()
  if not tareas:
    return make_response(jsonify({'message': 'Tareas no encontradas'}), 404)
  
  return make_response(jsonify(lista_tareas_schema.dump(tareas)), 200)

@tarea.route('/update/estado/<int:id_tarea>', methods=['PUT'])
def update_estado_tarea(id_tarea):
  
  tarea = Tarea.query.filter_by(id_tarea=id_tarea).first()
  if not tarea:
    return make_response(jsonify({'message': 'Tarea no encontrada'}), 404)
  
  tarea.estado = not tarea.estado
  db.session.commit()
  
  return make_response(jsonify({'message': 'Tarea actualizada'}), 200)

@tarea.route('/update/tecnico/<int:id_tarea>', methods=['PUT'])
def update_tecnico_tarea(id_tarea):
  data = request.get_json()
  id_tecnico = data['id_tecnico']
  
  if not id_tecnico:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  tarea = Tarea.query.filter_by(id_tarea=id_tarea).first()
  if not tarea:
    return make_response(jsonify({'message': 'Tarea no encontrada'}), 404)
  
  tarea.id_tecnico = id_tecnico
  db.session.commit()
  
  return make_response(jsonify({'message': 'Tarea actualizada'}), 200)