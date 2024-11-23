from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class OrdenServicioTecnico(db.Model):
  __tablename__ = 'orden_servicio_tecnico'
  
  id_ost = db.Column(db.Integer, primary_key=True)
  fecha_registro = db.Column(db.Date, nullable=False)
  estado = db.Column(db.Integer, nullable=False)
  fecha_aprox_ingreso = db.Column(db.Date, nullable=False)
  id_consulta = db.Column(db.Integer, db.ForeignKey('consulta.id_consulta'), nullable=False)
  
  lista_tareas = db.relationship('ListaTareas', backref='orden_servicio_tecnico', cascade = 'all, delete-orphan',lazy=True, uselist=False)
  informe_tecnico = db.relationship('InformeTecnico', backref='orden_servicio_tecnico', cascade = 'all, delete-orphan',lazy=True, uselist=False)
  ficha_salida = db.relationship('FichaSalida', backref='orden_servicio_tecnico', cascade = 'all, delete-orphan',lazy=True, uselist=False)
  ficha_ingreso = db.relationship('FichaIngreso', backref='orden_servicio_tecnico', cascade = 'all, delete-orphan',lazy=True, uselist=False)
  
  def __init__(self, id_consulta, fecha_aprox_ingreso):
    # self.id_ost = uuid4().int
    self.fecha_registro = datetime.now(timezone.utc) - timedelta(hours=5)
    self.estado = 1
    self.fecha_aprox_ingreso = fecha_aprox_ingreso
    self.id_consulta = id_consulta