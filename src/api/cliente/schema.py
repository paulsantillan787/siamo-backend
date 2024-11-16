from src.common.utils.ma import ma
from marshmallow import fields
from src.api.persona.schema import PersonaSchema, PersonaDetailSchema

class ClienteSchema(ma.Schema):
  id_cliente = fields.Integer()
  id_persona = fields.Integer()
  persona = fields.Nested(PersonaSchema)
  
cliente_schema = ClienteSchema()

class ClienteDetailSchema(ma.Schema):
  id_persona = fields.Integer()
  persona = fields.Nested(PersonaDetailSchema)
  
cliente_detail_schema = ClienteDetailSchema()
clientes_detail_schema = ClienteDetailSchema(many=True)
  