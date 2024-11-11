from src.common.utils.ma import ma
from marshmallow import fields
from src.api.repuesto.schema import RepuestoDetailSchema

class PresupuestoRespuestoSchema(ma.Schema):
  id_presupuesto = fields.Integer()
  id_respuesto = fields.Integer()
  cantidad = fields.Integer()
  
presupuesto_respuesto_schema = PresupuestoRespuestoSchema()

class PresupuestoRespuestoDetailSchema(ma.Schema):
  repuesto = fields.Nested(RepuestoDetailSchema)
  cantidad = fields.Integer()
  
presupuesto_respuesto_detail_schema = PresupuestoRespuestoDetailSchema(many=True)