from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)

    # Add config to the flask app
    app.config.from_object(config[config_name])

    # Register all the blueprints
    from .talks import talks as talk_blueprint
    app.register_blueprint(talk_blueprint)

    return app