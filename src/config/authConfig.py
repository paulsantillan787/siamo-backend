from appConfig import app
from flask_jwt_extended import JWTManager
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

jwt=JWTManager(app)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))