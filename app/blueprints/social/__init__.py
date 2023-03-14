from flask import Blueprint

bp = Blueprint('social', __name__)

from app.blueprints.social import routes