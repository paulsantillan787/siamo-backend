from src.common.utils.ma import ma
from marshmallow import fields

class RepuestoSchema(ma.Schema):
  id_repuesto = fields.Integer()
  descripcion = fields.String()
  precio = fields.Float()
  
repuesto_schema = RepuestoSchema()
repuestos_schema = RepuestoSchema(many=True)
  
class RepuestoDetailSchema(ma.Schema):
  descripcion = fields.String()
  precio = fields.Float()
  
repuesto_detail_schema = RepuestoDetailSchema()
