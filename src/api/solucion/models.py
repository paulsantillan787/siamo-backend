from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Solucion(db.Model):
  __tablename__ = 'solucion'
  
  id_solucion = db.Column(db.Integer, primary_key=True)
  descripcion = db.Column(db.String(250), nullable=False)
  
  problema = db.relationship('Problema', backref='solucion', cascade='all, delete-orphan', lazy=True, uselist=False)
  
  def __init__(self, descripcion):
    # self.id_solucion = uuid4().int
    self.descripcion = descripcion