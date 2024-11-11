from src.common.utils.ma import ma
from marshmallow import fields

class SolucionSchema(ma.Schema):
  descripcion = fields.String()
  
solucion_schema = SolucionSchema()