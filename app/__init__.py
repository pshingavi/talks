from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# Instantiate extentions
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # Add config to the flask app
    app.config.from_object(config[config_name])

    # Initialize with bootstrap
    bootstrap.init_app(app)

    # Initialize with SQLAlchemy
    db.init_app(app)

    # Register all the blueprints
    from .talks import talks as talk_blueprint
    app.register_blueprint(talk_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app