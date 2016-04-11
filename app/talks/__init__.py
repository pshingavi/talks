# Blueprints are containers for routes, static files and/or templates
from flask import Blueprint

# Define blueprint , define it's routes in routes.py and register the blueprint in app/__init__.py
talks = Blueprint('talks', __name__)
# The blueprint becomes a part of the application when it is registered

# Avoid circular dependencies
from . import routes
