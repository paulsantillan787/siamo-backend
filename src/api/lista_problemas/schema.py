from src.common.utils.ma import ma
from marshmallow import fields
from src.api.problema.schema import ProblemaSchema

class ListaProblemasSchema(ma.Schema):
  # id_consulta = fields.Integer()
  problema = fields.Nested(ProblemaSchema)
  
lista_problemas_schema = ListaProblemasSchema(many=True)