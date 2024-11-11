from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class Empleado(db.Model):
  __tablename__ = 'empleado'
  
  id_empleado = db.Column(db.Integer, primary_key=True)
  fecha_ingreso = db.Column(db.Date, nullable=False)
  cod_empleado = db.Column(db.Integer, nullable=False)
  contrasenia = db.Column(db.String(255), nullable=False)
  id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False)
  
  recepcionista = db.relationship('Recepcionista', backref='empleado', cascade = 'all, delete-orphan', lazy=True)
  tecnico = db.relationship('Tecnico', backref='empleado', cascade = 'all, delete-orphan', lazy=True)
  
  def __init__(self, fecha_ingreso, cod_empleado, contrasenia, id_persona):
    # self.id_empleado = uuid4().int
    self.fecha_ingreso = fecha_ingreso
    self.cod_empleado = cod_empleado
    self.contrasenia = contrasenia
    self.id_persona = id_persona
    