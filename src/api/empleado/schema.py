from src.common.utils.ma import ma
from marshmallow import fields
from src.api.persona.schema import PersonaSchema, PersonaDetailSchema

class EmpleadoSchema(ma.Schema):
  id_empleado = fields.Integer()
  # fecha_ingreso = fields.Date()
  # cod_empleado = fields.Integer()
  # contrasenia = fields.String()
  id_persona = fields.Integer()
  persona = fields.Nested(PersonaDetailSchema)
  
empleado_schema = EmpleadoSchema()

class EmpleadoDetailSchema(ma.Schema):
  cod_empleado = fields.Integer()
  persona = fields.Nested(PersonaDetailSchema)
  
empleado_detail_schema = EmpleadoDetailSchema()

class EmpleadoLoginSchema(ma.Schema):
  id_empleado = fields.Integer()
  cod_empleado = fields.Integer()
  contrasenia = fields.String()
  id_tecnico = fields.Integer()
  tipo = fields.Integer()

empleado_login_schema = EmpleadoLoginSchema()