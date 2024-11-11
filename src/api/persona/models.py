from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Persona(db.Model):
  __tablename__ = 'persona'
  
  id_persona = db.Column(db.Integer, primary_key=True)
  tipo_doc = db.Column(db.Boolean, nullable=False)
  num_doc = db.Column(db.String(8), nullable=False)
  nombres = db.Column(db.String(30), nullable=False)
  apellidos = db.Column(db.String(50), nullable=False)
  direccion = db.Column(db.String(100), nullable=False)
  sexo = db.Column(db.String(1), nullable=False)
  telefono = db.Column(db.String(9), nullable=False)
  correo = db.Column(db.String(50), nullable=False)
  
  empleado = db.relationship('Empleado', backref='persona', cascade = 'all, delete-orphan',lazy=True)
  cliente = db.relationship('Cliente', backref='persona', cascade = 'all, delete-orphan',lazy=True)
  
  def __init__(self, tipo_doc, num_doc, nombres, apellidos, direccion, sexo, telefono, correo):
    # self.id_persona = uuid4().int
    self.tipo_doc = tipo_doc
    self.num_doc = num_doc
    self.nombres = nombres
    self.apellidos = apellidos
    self.direccion = direccion
    self.sexo = sexo
    self.telefono = telefono
    self.correo = correo
  