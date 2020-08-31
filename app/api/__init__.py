""" API Blueprint Application """

from flask import Blueprint
from flask_restx import Api

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api_rest = Api(api_bp)


@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


# Import resources to ensure view is registered
from .users import * # NOQA
from .todos import * # NOQA
from .slacks import * # NOQA
from .security import * # NOQA
