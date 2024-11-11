from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Repuesto(db.Model):
  __tablename__ = 'repuesto'
  
  id_repuesto = db.Column(db.Integer, primary_key=True)
  descripcion = db.Column(db.String(50), nullable=False)
  precio = db.Column(db.Float, nullable=False)
  
  presupuesto_repuesto = db.relationship('PresupuestoRepuesto', backref='repuesto', cascade = 'all, delete-orphan',lazy=True)
  
  def __init__(self, descripcion, precio):
    # self.id_repuesto = uuid4().int
    self.descripcion = descripcion
    self.precio = precio