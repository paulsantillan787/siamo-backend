from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Tecnico(db.Model):
  __tablename__ = 'tecnico'
  
  id_tecnico = db.Column(db.Integer, primary_key=True)
  id_empleado = db.Column(db.Integer, db.ForeignKey('empleado.id_empleado'), nullable=False)
  
  consulta = db.relationship('Consulta', backref='tecnico', cascade = 'all, delete-orphan',lazy=True)
  # tarea = db.relationship('Tarea', backref='tecnico', cascade = 'all, delete-orphan',lazy=True)
  
  def __init__(self, id_empleado):
    # self.id_tecnico = uuid4().int
    self.id_empleado = id_empleado
  