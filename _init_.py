from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # IMPORT DES ROUTES (IMPORTANT)
    from app.routes.auth import auth
    from app.routes.content import content

    app.register_blueprint(auth)
    app.register_blueprint(content)

    return app