from flask_restful import Resource
from flask import request
from Models import db, Users
from KEY import KEY
from Encrytion import Encryption
from requests import Re


class Key(Resource):
    def get(username, self):
        user = Users.query.filter_by(username=username).first()
        key = user.key().get("encryption_key", 0)

        return {"status": "success", "data": key}, 200

    def post(self):
        json_data = request.get_json()

        if not json_data:
            return {"message": "No input data provided"}, 400

        user = Users.query.filter_by(username=json_data["username"]).first()
        if not user:
            return {"message": "Username not available"}, 400

        user = Users.query.filter_by(username=json_data["username"]).one()
        key = Users.key(user).get("encryption_key", 0)

        return {"status": "success", "data": key}, 200
