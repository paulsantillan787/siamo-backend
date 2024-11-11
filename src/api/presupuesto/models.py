from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Presupuesto(db.Model):
  __tablename__ = 'presupuesto'
  
  id_presupuesto = db.Column(db.Integer, primary_key=True)
  tarifa_mano_obra = db.Column(db.Float, nullable=False)
  tarifa_repuestos = db.Column(db.Float, nullable=False)
  descuento_negociado = db.Column(db.Float, nullable=False)
  id_consulta = db.Column(db.Integer, db.ForeignKey('consulta.id_consulta'), nullable=False)
  
  presupuesto_repuesto = db.relationship('PresupuestoRepuesto', backref='presupuesto', cascade = 'all, delete-orphan',lazy=True)
  
  
  def __init__(self, tarifa_mano_obra, tarifa_repuestos, descuento_negociado, id_consulta):
    # self.id_presupuesto = uuid4().int
    self.tarifa_mano_obra = tarifa_mano_obra
    self.tarifa_repuestos = tarifa_repuestos
    self.descuento_negociado = descuento_negociado
    self.id_consulta = id_consulta