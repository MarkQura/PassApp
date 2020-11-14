from flask import Blueprint
from flask_restful import Api
from resources.register import Register
from resources.pas import Pass
from resources.Encryption import Key

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Route
api.add_resource(Register, "/register")
api.add_resource(Pass, "/pass")
api.add_resource(Key, "/key")