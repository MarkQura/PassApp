from flask_restful import Resource
from flask import request
from Models import db, Users, Content
from KEY import KEY
from Encrytion import Encryption
from requests import Re
from sqlalchemy import update
import ast


class Pass(Resource):
    def get(self):
        json_data = request.get_json()

        user = Re.checkUser(json_data["username"])
        if not user:
            return {"message": "No username provided"}, 400

        passes = Content.query.filter_by(username=json_data["username"]).all()
        pass_list = []
        pas = {}
        for i in range(0, len(passes)):
            pas.update(passes[i].normal())
            encoded = passes[i].encoded()
            s = encoded.get("password", 0)
            user = Users.query.filter_by(username=json_data["username"]).one()
            key = Users.key(user).get("encryption_key", 0)
            decoded = Encryption.decoder(s.encode(), key)
            pas.update({"password": decoded})
            pass_list.append(ast.literal_eval(str(pas)))
            pas.clear()

        return {"status": "success", "data": pass_list}, 200

    def post(self):
        json_data = request.get_json()

        if not json_data:
            return {"message": "No data provided"}, 400

        user = Re.notUser(json_data["username"])
        if not user:
            return {"message": "Username not available"}, 400

        pas = KEY.password()
        passWord = Re.pas(json_data["username"], pas)
        web = Content.query.filter_by(webPage=json_data["webpage"]).first()
        uui = Re.uuid()

        passw = Content(
            uuid=uui,
            username=json_data["username"],
            passWord=passWord,
            webPage=json_data["webpage"],
            link=json_data["link"],
        )
        db.session.add(passw)
        db.session.commit()

        result = Content.serialize(passw)

        return {"status": "success", "data": result}