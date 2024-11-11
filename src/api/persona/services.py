from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Persona
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import persona_schema, persona_detail_schema

persona = Blueprint('persona', __name__)

@persona.route('/insert', methods=['POST'])
def insert_persona():
  data = request.get_json()
  tipo_doc = data['tipo_doc']
  num_doc = data['num_doc']
  nombres = data['nombres']
  apellidos = data['apellidos']
  direccion = data['direccion']
  sexo = data['sexo']
  telefono = data['telefono']
  correo = data['correo']
  
  if not tipo_doc or not num_doc or not nombres or not apellidos or not direccion or not sexo or not telefono or not correo:
    return make_response(jsonify({'message': 'Faltan datos'}), 400)
  
  persona = Persona.query.filter_by(tipo_doc=tipo_doc ,num_doc=num_doc).first()
  if persona:
    return make_response(jsonify({'message': 'La persona ya existe'}), 400)
  
  new_persona = Persona(tipo_doc, num_doc, nombres, apellidos, direccion, sexo, telefono, correo)
  db.session.add(new_persona)
  db.session.commit()
  
  return make_response(jsonify({'message': 'Persona creada', 'id': new_persona.id_persona}), 201)

@persona.route('/get//<int:id>', methods=['GET'])
def get_persona(id):
  persona = Persona.query.filter_by(id_persona=id).first()
  if not persona:
    return make_response(jsonify({'message': 'Persona no encontrada'}), 404)
  
  return make_response(jsonify(persona_schema.dump(persona)), 200)

@persona.route('/get/details/<int:id>', methods=['GET'])
def get_persona_details(id):
  persona = Persona.query.filter_by(id_persona=id).first()
  if not persona:
    return make_response(jsonify({'message': 'Persona no encontrada'}), 404)
  
  return make_response(jsonify(persona_detail_schema.dump(persona)), 200)