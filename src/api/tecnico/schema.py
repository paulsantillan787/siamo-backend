from src.common.utils.ma import ma
from marshmallow import fields
from src.api.empleado.schema import empleado_detail_schema

class TecnicoSchema(ma.Schema):
  id_tecnico = fields.Integer()
  id_empleado = fields.Integer()
  
tecnico_schema = TecnicoSchema()

class TecnicoDetailSchema(ma.Schema):
  id_empleado = fields.Integer()
  empleado = fields.Nested(empleado_detail_schema)
  
tecnico_detail_schema = TecnicoDetailSchema()