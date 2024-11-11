from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Problema(db.Model):
  __tablename__ = 'problema'
  
  id_problema = db.Column(db.Integer, primary_key=True)
  descripcion = db.Column(db.String(50), nullable=False)
  detalle = db.Column(db.String(250), nullable=False)
  id_solucion = db.Column(db.Integer, db.ForeignKey('solucion.id_solucion'), nullable=False)
  
  lista_problemas = db.relationship('ListaProblemas', backref='problema', cascade='all, delete-orphan', lazy=True)
  
  def __init__(self, descripcion, detalle, id_solucion):
    # self.id_problema = uuid4().int
    self.descripcion = descripcion
    self.detalle = detalle
    self.id_solucion = id_solucion