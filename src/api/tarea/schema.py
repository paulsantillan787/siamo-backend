from src.common.utils.ma import ma
from marshmallow import fields
from src.api.tecnico.schema import TecnicoDetailSchema

class TareasSchema(ma.Schema):
  id_tarea = fields.Integer()
  descripcion = fields.String()
  estado = fields.Boolean()
  tecnico = fields.Nested(TecnicoDetailSchema)
  
tareas_schema = TareasSchema()
lista_tareas_schema = TareasSchema(many=True)