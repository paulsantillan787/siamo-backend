from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class ListaTareas(db.Model):
  __tablename__ = 'lista_tareas'
  
  id_lista_tareas = db.Column(db.Integer, primary_key=True)
  id_ost = db.Column(db.Integer, db.ForeignKey('orden_servicio_tecnico.id_ost'), nullable=False)
  
  tarea = db.relationship('Tarea', backref='lista_tareas', cascade = 'all, delete-orphan',lazy=True)
  
  def __init__(self, id_ost):
    # self.id_lista_tareas = uuid4().int
    self.id_ost = id_ost