from flask import Blueprint, request, jsonify, make_response
from api.consulta.models import Consulta #ultima agregacion
from api.tecnico.models import Tecnico #ultima agregacion
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

# mostrar datos del grafico Estado OSTs
# @GET("api/osts/getDatosGraficoRecepcioniosta1/{mes}")
@ost.route('/getDatosGraficoRecepcionista1/<int:mes>', methods=['GET'])
def getDatosGraficoTecnico1(mes):
  osts = OrdenServicioTecnico.query.filter(
      db.extract('month', OrdenServicioTecnico.fecha_registro) == mes
  ).all()
  if not osts:
    return make_response(jsonify({'mensaje': 'Ordenes de servicio técnico no encontradas'}), 404)
  
  # Cuantificar el número de OSTS por estado
  # 1: Pendiente
  # 2: En proceso
  # 3: Finalizado
  # 4: Cancelado
  pendientes = 0
  en_proceso = 0
  finalizados = 0
  cancelados = 0

  for ost in osts:
    if ost.estado == 1:
      pendientes += 1
    elif ost.estado == 2:
      en_proceso += 1
    elif ost.estado == 3:
      finalizados += 1
    elif ost.estado == 4:
      cancelados += 1

  datos = [
        {'etiqueta': 'Pendientes', 'valor': float(pendientes)},
        {'etiqueta': 'En proceso', 'valor': float(en_proceso)},
        {'etiqueta': 'Finalizados', 'valor': float(finalizados)},
        {'etiqueta': 'Cancelados', 'valor': float(cancelados)}
    ]

  return make_response(jsonify(datos), 200)


# DASHBOARD RECEPCIONISTA
# mostrar datos del grafico N° OSTs por técnico
# @GET("api/osts/getDatosGraficoRecepcionista2/{mes}")
'''@ost.route('/getDatosGraficoRecepcionista2/<int:mes>', methods=['GET'])
def getDatosGraficoRecepcionista2(mes):
    osts = db.session.query(OrdenServicioTecnico, Consulta, Tecnico).join(
        Consulta, OrdenServicioTecnico.id_consulta == Consulta.id_consulta
    ).join(
        Tecnico, Consulta.id_tecnico == Tecnico.id_tecnico
    ).filter(
        db.extract('month', OrdenServicioTecnico.fecha_registro) == mes
    ).all()
    
    if not osts:
        return make_response(jsonify({'mensaje': 'Ordenes de servicio técnico no encontradas'}), 404)
    
    # Cuantificar el número de OSTS por técnico
    tecnicos = {}
    for ost, consulta, tecnico in osts:
        nombre_tecnico = f"Técnico {tecnico.id_tecnico}"  # Puedes ajustar esto para obtener el nombre real si está disponible
        if nombre_tecnico in tecnicos:
            tecnicos[nombre_tecnico] += 1
        else:
            tecnicos[nombre_tecnico] = 1

    datos = []
    for nombre_tecnico, cantidad in tecnicos.items():
        datos.append({'etiqueta': nombre_tecnico, 'valor': float(cantidad)})

    return make_response(jsonify(datos), 200)

# mostrar datos del grafico Consultas vs OSTs
# @GET("api/osts/getDatosGraficoRecepcionista3/{mes}")
@ost.route('/getDatosGraficoRecepcionista3/<int:mes>', methods=['GET'])
def getDatosGraficoRecepcionista3(mes):
    # Obtener el número de consultas registradas en el mes
    num_consultas = db.session.query(Consulta).filter(
        db.extract('month', Consulta.fecha_registro) == mes
    ).count()

    # Obtener el número de OSTs registradas en el mes
    num_osts = db.session.query(OrdenServicioTecnico).filter(
        db.extract('month', OrdenServicioTecnico.fecha_registro) == mes
    ).count()

    if num_consultas == 0 and num_osts == 0:
        return make_response(jsonify({'mensaje': 'Consultas y OSTs no encontradas'}), 404)

    datos = [
        {'etiqueta': 'Consultas', 'valor': float(num_consultas)},
        {'etiqueta': 'OSTs', 'valor': float(num_osts)}
    ]

    return make_response(jsonify(datos), 200)
'''