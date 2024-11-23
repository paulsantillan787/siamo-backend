from src.common.utils.ma import ma
from marshmallow import fields

class FichaSalidaSchema(ma.Schema):
  id_ficha_salida = fields.Integer()
  fecha_recojo = fields.DateTime()
  
ficha_salida_schema = FichaSalidaSchema()