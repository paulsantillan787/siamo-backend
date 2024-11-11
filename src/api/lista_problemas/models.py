from src.common.utils.db import db
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timedelta, timezone
from sqlalchemy import PrimaryKeyConstraint

@dataclass
class ListaProblemas(db.Model):
    __tablename__ = 'lista_problemas'
    
    id_consulta = db.Column(db.Integer, db.ForeignKey('consulta.id_consulta'), nullable = False)
    id_problema = db.Column(db.Integer, db.ForeignKey('problema.id_problema'), nullable = False)
    
    __table_args__ = (
        PrimaryKeyConstraint('id_consulta', 'id_problema'),
    )
    
    def __init__(self, id_consulta, id_problema):
        self.id_consulta = id_consulta
        self.id_problema = id_problema