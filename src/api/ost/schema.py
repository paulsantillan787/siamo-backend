from src.common.utils.ma import ma
from marshmallow import fields
from src.api.ficha_ingreso.schema import FichaIngresoSchema
from src.api.ficha_salida.schema import FichaSalidaSchema
from src.api.consulta.schema import ConsultaDetailSchema
from src.api.informe_tecnico.schema import InformeTecnicoResumedSchema

class OstSchema(ma.Schema):
  id_ost = fields.Integer()
  fecha_registro = fields.Date()
  estado = fields.String()
  id_consulta = fields.Integer()
  fecha_aprox_ingreso = fields.Date()
  consulta = fields.Nested(ConsultaDetailSchema)
  informe_tecnico = fields.Nested(InformeTecnicoResumedSchema)
  ficha_ingreso = fields.Nested(FichaIngresoSchema)
  ficha_salida = fields.Nested(FichaSalidaSchema)
  
ost_schema = OstSchema()

class OstMenuSchema(ma.Schema):
  id_ost = fields.Integer()
  id_consulta = fields.Integer()
  ficha_ingreso = fields.Nested(FichaIngresoSchema)
  
ost_menu_schema = OstMenuSchema()
lista_ost_menu_schema = OstMenuSchema(many=True)