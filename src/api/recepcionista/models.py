from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Recepcionista(db.Model):
  __tablename__ = 'recepcionista'
  
  id_recepcionista = db.Column(db.Integer, primary_key=True)
  id_empleado = db.Column(db.Integer, db.ForeignKey('empleado.id_empleado'), nullable=False)
  
  def __init__(self, id_empleado):
    # self.id_recepcionista = uuid4().int
    self.id_empleado = id_empleado