from src.common.utils.ma import ma
from marshmallow import fields

class EmpleadoSchema(ma.Schema):
  id_empleado = fields.Integer()
  fecha_ingreso = fields.Date()
  cod_empleado = fields.Integer()
  contrasenia = fields.String()
  id_persona = fields.Integer()
  
empleado_schema = EmpleadoSchema()

class EmpleadoDetailSchema(ma.Schema):
  cod_empleado = fields.Integer()
  contrasenia = fields.String()
  
empleado_detail_schema = EmpleadoDetailSchema()