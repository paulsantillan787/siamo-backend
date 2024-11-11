from src.common.utils.ma import ma
from marshmallow import fields
from src.api.persona.schema import PersonaSchema

class ClienteSchema(ma.Schema):
  id_cliente = fields.Integer()
  id_persona = fields.Integer()
  
cliente_schema = ClienteSchema()

class ClienteDetailSchema(ma.Schema):
  id_persona = fields.Integer()
  persona = fields.Nested(PersonaSchema)
  
cliente_detail_schema = ClienteDetailSchema()
  