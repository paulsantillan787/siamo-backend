from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Imprevisto(db.Model):
  __tablename__ = 'imprevisto'
  
  id_imprevisto = db.Column(db.Integer, primary_key=True)
  descripcion = db.Column(db.String(300), nullable=False)
  solucion = db.Column(db.String(300), nullable=False)
  precio = db.Column(db.Float, nullable=False)
  
  informe_tecnico = db.relationship('InformeTecnico', backref='imprevisto', cascade = 'all, delete-orphan',lazy=True)
  
  def __init__(self, descripcion, solucion, precio):
    self.id_imprevisto = uuid4().int
    self.descripcion = descripcion
    self.solucion = solucion
    self.precio = precio