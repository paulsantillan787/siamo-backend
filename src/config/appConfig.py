from flask import Flask
from src.common.utils.db import db
from src.config.databaseConfig import DATABASE_CONNECTION
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
# from src.api.user.services import users
# from src.api.template_test.services import template_tests
# from src.api.question.services import questions
# from src.api.alternative.services import alternatives
# from src.api.clasification.services import clasifications
# from src.api.test.services import tests
# from src.api.answer.services import answers
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

# app.register_blueprint(users, url_prefix='/api/users')
# app.register_blueprint(template_tests, url_prefix='/api/template_tests')
# app.register_blueprint(questions, url_prefix='/api/questions')
# app.register_blueprint(alternatives, url_prefix='/api/alternatives')
# app.register_blueprint(clasifications, url_prefix='/api/clasifications')
# app.register_blueprint(tests, url_prefix='/api/tests')
# app.register_blueprint(answers, url_prefix='/api/answers')

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

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()