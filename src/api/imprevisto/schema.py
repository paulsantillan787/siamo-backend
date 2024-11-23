from src.common.utils.ma import ma
from marshmallow import fields

class ImprevistoSchema(ma.Schema):
  id_imprevisto = fields.Integer()
  descripcion = fields.String()
  solucion = fields.String()
  precio = fields.Float()
  
imprevisto_schema = ImprevistoSchema()