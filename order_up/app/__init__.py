from flask import Flask
from flask_login import LoginManager
from .routes import bp
from .config import Config
from .models import db, Employee

flask_app = Flask(__name__)
flask_app.config.from_object(Config)
flask_app.register_blueprint(bp)

db.init_app(flask_app)

login = LoginManager(flask_app)
login.login_view = "session.login"

@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
