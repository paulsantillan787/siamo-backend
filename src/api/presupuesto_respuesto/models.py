from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone
from sqlalchemy import PrimaryKeyConstraint

@dataclass
class PresupuestoRepuesto(db.Model):
  __tablename__ = 'presupuesto_respuesto'
  
  id_presupuesto = db.Column(db.Integer, db.ForeignKey('presupuesto.id_presupuesto'),nullable=False,)
  id_respuesto = db.Column(db.Integer, db.ForeignKey('repuesto.id_repuesto'), nullable=False,)
  cantidad = db.Column(db.Integer, nullable=False,)
  
  __table_args__ = (
    PrimaryKeyConstraint('id_presupuesto', 'id_respuesto'),
  )
  
  def __init__(self, id_presupuesto, id_respuesto, cantidad):
    self.id_presupuesto = id_presupuesto
    self.id_respuesto = id_respuesto
    self.cantidad = cantidad