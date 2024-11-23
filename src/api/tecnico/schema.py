from src.common.utils.ma import ma
from marshmallow import fields
from src.api.empleado.schema import EmpleadoDetailSchema, EmpleadoSchema

class TecnicoSchema(ma.Schema):
  id_tecnico = fields.Integer()
  # id_empleado = fields.Integer()
  empleado = fields.Nested(EmpleadoSchema)
  ost_count = fields.Integer()
  
tecnico_schema = TecnicoSchema()
tecnicos_schema = TecnicoSchema(many=True)

class TecnicoDetailSchema(ma.Schema):
  id_empleado = fields.Integer()
  empleado = fields.Nested(EmpleadoDetailSchema)
  
tecnico_detail_schema = TecnicoDetailSchema()