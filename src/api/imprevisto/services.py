from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Imprevisto
from src.api.informe_tecnico.models import InformeTecnico
from .schema import imprevisto_schema
from src.common.utils.db import db
from src.common.utils.data import data

imprevisto = Blueprint('imprevisto', __name__)

@imprevisto.route('/insert/<int:id_informe_tecnico>', methods=['POST'])
def insert_imprevisto(id_informe_tecnico):
  data = request.get_json()
  descripcion = data['descripcion']
  solucion = data['solucion']
  precio = data['precio']
  
  if not descripcion or not solucion or not precio:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  new_imprevisto = Imprevisto(descripcion, solucion, precio)
  db.session.add(new_imprevisto)
  db.session.commit()
  
  informe = InformeTecnico.query.filter_by(id_informe_tecnico=id_informe_tecnico).first()
  if not informe:
    return make_response(jsonify({'mensaje': 'Informe técnico no encontrado'}), 404)
  
  informe.id_imprevisto = new_imprevisto.id_imprevisto
  informe.saldo_final = informe.saldo_final + precio
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Imprevisto creado', 'id': new_imprevisto.id_imprevisto}), 201)

@imprevisto.route('/get/<int:id_imprevisto>', methods=['GET'])
def get_imprevisto(id_imprevisto):
  imprevisto = Imprevisto.query.filter_by(id_imprevisto=id_imprevisto).first()
  if not imprevisto:
    return make_response(jsonify({'mensaje': 'Imprevisto no encontrado'}), 404)
  
  return make_response(jsonify(imprevisto_schema.dump(imprevisto)), 200)

@imprevisto.route('/update/<int:id_imprevisto>', methods=['PUT'])
def update_imprevisto(id_imprevisto):
  data = request.get_json()
  descripcion = data['descripcion']
  solucion = data['solucion']
  precio = data['precio']
  
  if not descripcion or not solucion or not precio:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  imprevisto = Imprevisto.query.filter_by(id_imprevisto=id_imprevisto).first()
  if not imprevisto:
    return make_response(jsonify({'mensaje': 'Imprevisto no encontrado'}), 404)
  
  imprevisto.descripcion = descripcion
  imprevisto.solucion = solucion
  imprevisto.precio = precio
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Imprevisto actualizado'}), 200)