from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import FichaIngreso
from src.api.ost.models import OrdenServicioTecnico
from src.api.persona.models import Persona
from src.api.automovil.models import Automovil
from .schema import ficha_ingreso_schema
from .schema import ficha_ingreso_completa_schema
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


@ficha_ingreso.route('/get_full_data_by_tecnico/<int:id_tecnico>', methods=['GET'])
def get_full_fichas_ingreso_by_tecnico(id_tecnico):
    try:
        # Realizas la consulta uniendo las tablas
        fichas = db.session.query(
            FichaIngreso.id_ficha_ingreso,
            OrdenServicioTecnico.id_ost,
            Persona.nombre.label('nombre_cliente'),
            Automovil.placa.label('placa_vehiculo')
        ).join(
            OrdenServicioTecnico, FichaIngreso.id_ost == OrdenServicioTecnico.id_ost
        ).join(
            Consulta, OrdenServicioTecnico.id_consulta == Consulta.id_consulta
        ).join(
            Persona, Consulta.id_cliente == Persona.id_persona
        ).join(
            Automovil, Consulta.id_automovil == Automovil.id_automovil
        ).filter(
            Consulta.id_tecnico == id_tecnico
        ).all()

        if not fichas:
            return make_response(jsonify({'mensaje': 'No se encontraron fichas de ingreso para este técnico'}), 404)

        result = ficha_ingreso_completa_schema.dump(fichas)

    
        return make_response(jsonify(result), 200)

    except Exception as e:
        return make_response(jsonify({'mensaje': 'Error al obtener los datos', 'error': str(e)}), 500)

