from src.common.utils.ma import ma
from marshmallow import fields
from src.api.empleado.schema import empleado_detail_schema

class RecepcionistaSchema(ma.Schema):
  id_recepcionista = fields.Integer()
  id_empleado = fields.Integer()

recepcionista_schema = RecepcionistaSchema()

class RecepcionistaDetailSchema(ma.Schema):
  id_empleado = fields.Integer()
  empleado = fields.Nested(empleado_detail_schema)
  
recepcionista_detail_schema = RecepcionistaDetailSchema()
  