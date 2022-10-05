from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
bootstrap = Bootstrap(app)

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app import routes, models
