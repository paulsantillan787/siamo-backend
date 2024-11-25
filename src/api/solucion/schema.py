from src.common.utils.ma import ma
from marshmallow import fields

class SolucionSchema(ma.Schema):
  id_solucion = fields.Integer()
  descripcion = fields.String()
  
solucion_schema = SolucionSchema()