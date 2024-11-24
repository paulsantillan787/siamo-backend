from src.common.utils.ma import ma
from marshmallow import fields
# from src.api.ficha_ingreso.schema import FichaIngresoSchema, FichaIngresoDetailSchema

class EstadoVehiculoSchema(ma.Schema):
  id_estado_vehiculo = fields.Integer()
  estado_carroceria = fields.String()
  estado_neumaticos = fields.String()
  estado_motor = fields.String()
  estado_frenos = fields.String()
  # id_ficha_ingreso = fields.Integer()
  
estado_vehiculo_schema = EstadoVehiculoSchema()