from src.common.utils.ma import ma
from marshmallow import fields
from src.api.ficha_ingreso.schema import FichaIngresoSchema

class OstSchema(ma.Schema):
  id_ost = fields.Integer()
  fecha_registro = fields.Date()
  estado = fields.String()
  id_consulta = fields.Integer()
  fecha_aprox_ingreso = fields.Date()
  
ost_schema = OstSchema()

class OstMenuSchema(ma.Schema):
  id_ost = fields.Integer()
  id_consulta = fields.Integer()
  ficha_ingreso = fields.Nested(FichaIngresoSchema)
  
ost_menu_schema = OstMenuSchema()
lista_ost_menu_schema = OstMenuSchema(many=True)