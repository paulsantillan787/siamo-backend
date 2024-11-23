from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class FichaSalida(db.Model):
  __tablename__ = 'ficha_salida'
  
  id_ficha_salida = db.Column(db.Integer, primary_key=True)
  fecha_recojo = db.Column(db.DateTime, nullable=False)
  id_ost = db.Column(db.Integer, db.ForeignKey('orden_servicio_tecnico.id_ost'), nullable=False)
  
  def __init__(self, id_ost):
    # self.id_ficha_salida = uuid4().int
    self.fecha_recojo = datetime.now(timezone.utc) - timedelta(hours=5)
    self.id_ost = id_ost