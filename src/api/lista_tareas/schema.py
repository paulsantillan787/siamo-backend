from src.common.utils.ma import ma
from marshmallow import fields
from src.api.tarea.schema import TareasSchema

class ListaTareasSchema(ma.Schema):
  id_lista_tareas = fields.Integer()
  id_ost = fields.Integer()
  tarea = fields.List(fields.Nested(TareasSchema))

lista_tareas_schema = ListaTareasSchema()
listas_tareas_schema = ListaTareasSchema(many=True)