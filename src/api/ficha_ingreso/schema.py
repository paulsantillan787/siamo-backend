from src.common.utils.ma import ma
from marshmallow import fields
from src.api.estado_vehiculo.schema import EstadoVehiculoSchema

class FichaIngresoSchema(ma.Schema):
  id_ficha_ingreso = fields.Integer()
  fecha_ingreso = fields.DateTime()
  fecha_aprox_recojo = fields.Date()
  estado_vehiculo = fields.Nested(EstadoVehiculoSchema)
  
ficha_ingreso_schema = FichaIngresoSchema()
  
class FichaIngresoCompletaSchema(ma.Schema):
    id_ficha_ingreso = fields.Integer()
    id_ost = fields.Integer()
    nombre_cliente = fields.String()
    placa_vehiculo = fields.String()

ficha_ingreso_completa_schema = FichaIngresoCompletaSchema()