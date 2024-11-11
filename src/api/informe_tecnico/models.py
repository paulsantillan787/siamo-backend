from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone

@dataclass
class InformeTecnico(db.Model):
  __tablename__ = 'informe_tecnico'
  
  id_informe_tecnico = db.Column(db.Integer, primary_key=True)
  fecha_inicio_reparacion = db.Column(db.Date, nullable=False)
  fecha_fin_reparacion = db.Column(db.Date, nullable=False)
  detalle_reparacion = db.Column(db.String(250), nullable=False)
  observaciones = db.Column(db.String(300), nullable=False)
  # Analizar si el saldo_final debe permancer en la bd
  saldo_final = db.Column(db.Float, nullable=False)
  id_ost = db.Column(db.Integer, db.ForeignKey('orden_servicio_tecnico.id_ost'), nullable=False)
  id_imprevisto = db.Column(db.Integer, db.ForeignKey('imprevisto.id_imprevisto'), nullable=False)
  
  def __init__ (self, fecha_inicio_reparacion, fecha_fin_reparacion, detalle_reparacion, observaciones, saldo_final, id_ost, id_imprevisto):
    self.id_informe_tecnico = uuid4().int
    self.fecha_inicio_reparacion = fecha_inicio_reparacion
    self.fecha_fin_reparacion = fecha_fin_reparacion
    self.detalle_reparacion = detalle_reparacion
    self.observaciones = observaciones
    self.saldo_final = saldo_final
    self.id_ost = id_ost
    self.id_imprevisto = id_imprevisto