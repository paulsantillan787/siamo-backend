from src.common.utils.ma import ma
from marshmallow import fields
from src.api.cliente.schema import ClienteDetailSchema
from src.api.automovil.schema import AutomovilDetailSchema

class ConsultaSchema(ma.Schema):
  id_consulta = fields.Integer()
  prob_declarado = fields.String()
  estado = fields.Integer()
  id_cliente = fields.Integer()
  id_tecnico = fields.Integer()
  id_automovil = fields.Integer()
  
consulta_schema = ConsultaSchema()

class ConsultaDetailSchema(ma.Schema):
  cliente = fields.Nested(ClienteDetailSchema)
  automovil = fields.Nested(AutomovilDetailSchema)
  prob_declarado = fields.String()
  estado = fields.Integer()
  
consulta_detail_schema = ConsultaDetailSchema()
consultas_detail_schema = ConsultaDetailSchema(many=True)
