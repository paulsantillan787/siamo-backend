from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class FichaIngreso(db.Model):
  __tablename__ = 'ficha_ingreso'
  
  id_ficha_ingreso = db.Column(db.Integer, primary_key=True)
  fecha_ingreso = db.Column(db.DateTime, nullable=False)
  fecha_aprox_recojo = db.Column(db.Date, nullable=False)
  id_ost = db.Column(db.Integer, db.ForeignKey('orden_servicio_tecnico.id_ost'), nullable=False)
  
  estado_vehiculo = db.relationship('EstadoVehiculo', backref='ficha_ingreso', cascade = 'all, delete-orphan',lazy=True, uselist=False)
  
  def __init__(self, fecha_aprox_recojo, id_ost):
    # self.id_ficha_ingreso = uuid4().int
    self.fecha_ingreso = datetime.now(timezone.utc) - timedelta(hours=5)
    self.fecha_aprox_recojo = fecha_aprox_recojo
    self.id_ost = id_ost
    