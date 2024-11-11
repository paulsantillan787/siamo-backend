from src.common.utils.ma import ma
from marshmallow import fields

class PresupuestoSchema(ma.Schema):
  id_presupuesto = fields.Integer()
  tarifa_mano_obra = fields.Float()
  tarifa_repuestos = fields.Float()
  descuento_negociado = fields.Float()
  id_consulta = fields.Integer()
  
presupuesto_schema = PresupuestoSchema()