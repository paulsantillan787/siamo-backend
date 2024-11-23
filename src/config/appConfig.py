from flask import Flask
from src.common.utils.db import db
from src.config.databaseConfig import DATABASE_CONNECTION
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
from src.api.persona.services import persona
from src.api.empleado.services import empleado
from src.api.recepcionista.services import recepcionista
from src.api.tecnico.services import tecnico
from src.api.cliente.services import cliente
from src.api.automovil.services import automovil
from src.api.problema.services import problema
from src.api.solucion.services import solucion
from src.api.lista_problemas.services import lista_problemas
from src.api.consulta.services import consulta
from src.api.repuesto.services import repuesto
from src.api.presupuesto.services import presupuesto
from src.api.presupuesto_respuesto.services import presupuesto_respuesto
from src.api.estado_vehiculo.services import estado_vehiculo
from src.api.informe_tecnico.services import informe_tecnico
from src.api.ficha_ingreso.services import ficha_ingreso
from src.api.ficha_salida.services import ficha_salida
from src.api.imprevisto.services import imprevisto
from src.api.lista_tareas.services import lista_tareas
from src.api.tarea.services import tarea
from src.api.ost.services import ost

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": os.getenv("CORS_ORIGINS")}})

jwt = JWTManager(app)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))

app.register_blueprint(persona, url_prefix='/api/persona')
app.register_blueprint(empleado, url_prefix='/api/empleado')
app.register_blueprint(recepcionista, url_prefix='/api/recepcionista')
app.register_blueprint(tecnico, url_prefix='/api/tecnico')
app.register_blueprint(cliente, url_prefix='/api/cliente')
app.register_blueprint(automovil, url_prefix='/api/automovil')
app.register_blueprint(problema, url_prefix='/api/problema')
app.register_blueprint(solucion, url_prefix='/api/solucion')
app.register_blueprint(lista_problemas, url_prefix='/api/lista_problemas')
app.register_blueprint(consulta, url_prefix='/api/consulta')
app.register_blueprint(repuesto, url_prefix='/api/repuesto')
app.register_blueprint(presupuesto, url_prefix='/api/presupuesto')
app.register_blueprint(presupuesto_respuesto, url_prefix='/api/presupuesto_respuesto')
app.register_blueprint(estado_vehiculo, url_prefix='/api/estado_vehiculo')
app.register_blueprint(ficha_ingreso, url_prefix='/api/ficha_ingreso')
app.register_blueprint(ficha_salida, url_prefix='/api/ficha_salida')
app.register_blueprint(imprevisto, url_prefix='/api/imprevisto')
app.register_blueprint(lista_tareas, url_prefix='/api/lista_tareas')
app.register_blueprint(tarea, url_prefix='/api/tarea')
app.register_blueprint(ost, url_prefix='/api/ost')
app.register_blueprint(informe_tecnico, url_prefix='/api/informe_tecnico')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()