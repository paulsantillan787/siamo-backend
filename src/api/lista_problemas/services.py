from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import ListaProblemas
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import lista_problemas_schema

lista_problemas = Blueprint('lista_problemas', __name__)

@lista_problemas.route('/insert', methods=['POST'])
def insert_lista_problemas():
  data = request.get_json()
  id_consulta = data['id_consulta']
  # Lista de ids
  problemas = data['problemas']
  
  if not id_consulta or not problemas:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  for problema in problemas:
    new_lista_problemas = ListaProblemas(id_consulta, problema['id_problema'])
    db.session.add(new_lista_problemas)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Lista de problemas creada'}), 201)

@lista_problemas.route('/get/<int:id>', methods=['GET'])
def get_lista_problemas(id):
  lista_problemas = ListaProblemas.query.filter_by(id_consulta=id).all()
  if not lista_problemas:
    return make_response(jsonify({'message': 'Lista de problemas no encontrada'}), 404)
  
  return make_response(jsonify(lista_problemas_schema.dump(lista_problemas)), 200)