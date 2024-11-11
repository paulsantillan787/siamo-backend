from src.common.utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema):
  id_persona = fields.Integer()
  tipo_doc = fields.Boolean()
  num_doc = fields.String()
  nombres = fields.String()
  apellidos = fields.String()
  direccion = fields.String()
  sexo = fields.String()
  telefono = fields.String()
  correo = fields.String()

persona_schema = PersonaSchema()

class PersonaDetailSchema(ma.Schema):
  tipo_doc = fields.Boolean()
  num_doc = fields.String()
  nombres = fields.String()
  apellidos = fields.String()
  
persona_detail_schema = PersonaDetailSchema()