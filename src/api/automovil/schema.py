from src.common.utils.ma import ma
from marshmallow import fields

class AutomovilSchema(ma.Schema):
  id_automovil = fields.Integer()
  placa = fields.String()
  marca = fields.String()
  modelo = fields.String()
  id_cliente = fields.Integer()
  
automovil_schema = AutomovilSchema()

class AutomovilDetailSchema(ma.Schema):
  # placa = fields.String()
  marca = fields.String()
  modelo = fields.String()
  
automovil_detail_schema = AutomovilDetailSchema()