from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Consulta(db.Model):
  __tablename__ = 'consulta'
  
  id_consulta = db.Column(db.Integer, primary_key=True)
  prob_declarado = db.Column(db.String(200), nullable=False)
  estado = db.Column(db.Integer, nullable=False)
  id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'),nullable=False)
  id_tecnico = db.Column(db.Integer, db.ForeignKey('tecnico.id_tecnico'),nullable=False)
  id_automovil = db.Column(db.Integer, db.ForeignKey('automovil.id_automovil'),nullable=False)
  
  lista_problemas = db.relationship('ListaProblemas', backref='consulta', cascade = 'all, delete-orphan', lazy=True)
  presupuesto = db.relationship('Presupuesto', backref='consulta', cascade = 'all, delete-orphan', lazy=True)
  ost = db.relationship('OrdenServicioTecnico', backref='consulta', cascade = 'all, delete-orphan', lazy=True)
  
  def __init__(self, prob_declarado, estado, id_cliente, id_tecnico, id_automovil):
    # self.id_consulta = uuid4().int
    self.prob_declarado = prob_declarado
    self.estado = estado
    self.id_cliente = id_cliente
    self.id_tecnico = id_tecnico
    self.id_automovil = id_automovil
    