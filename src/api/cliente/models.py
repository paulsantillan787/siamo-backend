from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Cliente(db.Model):
  __tablename__ = 'cliente'
  
  id_cliente = db.Column(db.Integer, primary_key=True)
  id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False)
  
  automovil = db.relationship('Automovil', backref='cliente', cascade = 'all, delete-orphan',lazy=True)
  # Revisar si se elimina
  consulta = db.relationship('Consulta', backref='cliente', cascade = 'all, delete-orphan',lazy=True)
  
  def __init__(self, id_persona):
    # self.id_cliente = uuid4().int
    self.id_persona = id_persona