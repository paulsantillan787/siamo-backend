from src.common.utils.ma import ma
from marshmallow import fields
from src.api.imprevisto.schema import ImprevistoSchema

class InformeTecnicoSchema(ma.Schema):
  id_informe_tecnico = fields.Integer()
  fecha_inicio_reparacion = fields.Date()
  fecha_fin_reparacion = fields.Date()
  detalle_reparacion = fields.String()
  observaciones = fields.String()
  saldo_final = fields.Float()
  id_ost = fields.Integer()
  
  imprevisto = fields.Nested(ImprevistoSchema)
  
informe_tecnico_schema = InformeTecnicoSchema()

class InformeTecnicoResumedSchema(ma.Schema):
  id_informe_tecnico = fields.Integer()
  fecha_inicio_reparacion = fields.Date()
  fecha_fin_reparacion = fields.Date()
  detalle_reparacion = fields.String()
  observaciones = fields.String()
  saldo_final = fields.Float()
  # id_ost = fields.Integer()
  
informe_tecnico_resumed_schema = InformeTecnicoResumedSchema()