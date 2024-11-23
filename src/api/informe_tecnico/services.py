from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import InformeTecnico
from src.api.ost.models import OrdenServicioTecnico
from src.api.consulta.models import Consulta
from src.api.presupuesto.models import Presupuesto
from src.api.imprevisto.models import Imprevisto
from .schema import informe_tecnico_schema
from src.common.utils.db import db
from src.common.utils.data import data
from sqlalchemy.orm import joinedload

informe_tecnico = Blueprint('informe_tecnico', __name__)

@informe_tecnico.route('/insert', methods=['POST'])
def insert_informe_tecnico():
  data = request.get_json()
  fecha_inicio_reparacion = data['fecha_inicio_reparacion']
  fecha_fin_reparacion = data['fecha_fin_reparacion']
  detalle_reparacion = data['detalle_reparacion']
  observaciones = data['observaciones']
  # saldo_final = data['saldo_final']
  id_ost = data['id_ost']
  
  result = db.session.query(
        Presupuesto.tarifa_mano_obra, 
        Presupuesto.tarifa_repuestos, 
        Presupuesto.descuento_negociado
    ).join(
        Consulta, Consulta.id_consulta == Presupuesto.id_consulta
    ).join(
        OrdenServicioTecnico, OrdenServicioTecnico.id_consulta == Consulta.id_consulta
    ).filter(
        OrdenServicioTecnico.id_ost == id_ost
    ).first()

  if not result:
        return make_response(jsonify({'mensaje': 'Orden de servicio técnico, consulta o presupuesto no encontrado'}), 404)
    
  tarifa_mano_obra, tarifa_repuestos, descuento_negociado = result
  saldo_final = tarifa_mano_obra + tarifa_repuestos - descuento_negociado
  
  if not fecha_inicio_reparacion or not fecha_fin_reparacion or not detalle_reparacion or not observaciones or not saldo_final or not id_ost:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  new_informe_tecnico = InformeTecnico(fecha_inicio_reparacion, fecha_fin_reparacion, detalle_reparacion, observaciones, saldo_final, id_ost)
  db.session.add(new_informe_tecnico)
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Informe técnico creado', 'id': new_informe_tecnico.id_informe_tecnico}), 201)

@informe_tecnico.route('/get/<int:id_ost>', methods=['GET'])
def get_informe_tecnico_by_ost(id_ost):
  informe_tecnico = InformeTecnico.query.filter_by(id_ost=id_ost).first()
  if not informe_tecnico:
    return make_response(jsonify({'mensaje': 'Informe técnico no encontrado'}), 404)
  
  return make_response(jsonify(informe_tecnico_schema.dump(informe_tecnico)), 200)

@informe_tecnico.route('/update/<int:id_informe_tecnico>', methods=['PUT'])
def insert_imprevisto_to_informe_tecnico(id_informe_tecnico):
  data = request.get_json()
  id_imprevisto = data['id_imprevisto']
  
  if not id_imprevisto:
    return make_response(jsonify({'mensaje': 'Faltan datos'}), 400)
  
  informe_tecnico = InformeTecnico.query.filter_by(id_informe_tecnico=id_informe_tecnico).first()
  if not informe_tecnico:
    return make_response(jsonify({'mensaje': 'Informe técnico no encontrado'}), 404)
  
  informe_tecnico.id_imprevisto = id_imprevisto
  informe_tecnico.saldo_final = informe_tecnico.saldo_final + Imprevisto.query.filter_by(id_imprevisto=id_imprevisto).first().precio
  db.session.commit()
  
  return make_response(jsonify({'mensaje': 'Imprevisto añadido al informe técnico'}), 200)

