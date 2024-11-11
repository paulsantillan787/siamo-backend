from src.common.utils.ma import ma
from marshmallow import fields
from src.api.solucion.schema import SolucionSchema

class ProblemaSchema(ma.Schema):
  id_problema = fields.Integer()
  descripcion = fields.String()
  detalle = fields.String()
  
problema_schema = ProblemaSchema()

class ProblemaDetailSchema(ma.Schema):
  descripcion = fields.String()
  detalle = fields.String()
  solucion = fields.Nested(SolucionSchema)
  
problema_detail_schema = ProblemaDetailSchema()
problemas_detail_schema = ProblemaDetailSchema(many=True)