from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime,timedelta, timezone

@dataclass
class Automovil(db.Model):
  __tablename__ = 'automovil'
  
  id_automovil = db.Column(db.Integer, primary_key=True)
  placa = db.Column(db.String(8), nullable=False)
  marca = db.Column(db.String(15), nullable=False)
  modelo = db.Column(db.String(50), nullable=False)
  id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
  
  consulta = db.relationship('Consulta', backref='automovil', cascade = 'all, delete-orphan',lazy=True)
  
  def __init__(self, placa, marca, modelo, id_cliente):
    # self.id_automovil = uuid4().int
    self.placa = placa
    self.marca = marca
    self.modelo = modelo
    self.id_cliente = id_cliente