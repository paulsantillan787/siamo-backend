from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Tarea(db.Model):
  __tablename__ = 'tarea'
  
  id_tarea = db.Column(db.Integer, primary_key=True)
  descripcion = db.Column(db.String(50), nullable=False)
  estado = db.Column(db.Boolean, nullable=False)
  id_lista_tareas = db.Column(db.Integer, db.ForeignKey('lista_tareas.id_lista_tareas'), nullable=False)
  id_tecnico = db.Column(db.Integer, db.ForeignKey('tecnico.id_tecnico'), nullable=False)
  
  def __init__(self, descripcion, id_lista_tareas, id_tecnico):
    self.id_tarea = uuid4().int
    self.descripcion = descripcion
    self.estado = False
    self.id_lista_tareas = id_lista_tareas
    self.id_tecnico = id_tecnico
  