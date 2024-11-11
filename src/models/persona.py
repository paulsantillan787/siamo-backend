
from src.common.utils.db import db

class Persona(db.Model):
    # ...existing code...
    empleado = db.relationship('Empleado', backref='persona', uselist=False)
    # ...existing code...