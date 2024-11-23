from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class EstadoVehiculo(db.Model):
  __tablename__ = 'estado_vehiculo'
  
  id_estado_vehiculo = db.Column(db.Integer, primary_key=True)
  estado_carroceria = db.Column(db.String(200), nullable=False)
  estado_neumaticos = db.Column(db.String(200), nullable=False)
  estado_motor = db.Column(db.String(200), nullable=False)
  estado_frenos = db.Column(db.String(200), nullable=False)
  id_ficha_ingreso = db.Column(db.Integer, db.ForeignKey('ficha_ingreso.id_ficha_ingreso'), nullable=False)
  
  def __init__(self, estado_carroceria, estado_neumaticos, estado_motor, estado_frenos, id_ficha_ingreso):
    # self.id_estado_vehiculo = uuid4().int
    self.estado_carroceria = estado_carroceria
    self.estado_neumaticos = estado_neumaticos
    self.estado_motor = estado_motor
    self.estado_frenos = estado_frenos
    self.id_ficha_ingreso = id_ficha_ingreso