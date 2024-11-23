from src.common.utils.ma import ma
from marshmallow import fields

class FichaIngresoSchema(ma.Schema):
  id_ficha_ingreso = fields.Integer()
  fecha_ingreso = fields.DateTime()
  fecha_aprox_recojo = fields.Date()
  
ficha_ingreso_schema = FichaIngresoSchema()
  
  