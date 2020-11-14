from flask_restful import Resource
from flask import request
from Models import db, Users
from KEY import KEY
from Encrytion import Encryption
from requests import Re
import ast


class Register(Resource):
    def get(self):
        users = Users.query.all()
        user = {}
        user_list = []

        for i in range(0, len(users)):
            normal = users[i].normal()
            user.update(normal)

            key = users[i].key().get("encryption_key", 0)
            user1 = users[i].encoded()
            for b, c in user1.items():
                d = Encryption.decoder(c.encode(), key)
                user.update(
                    {
                        b: d,
                    }
                )
            user_list.append(ast.literal_eval(str(user)))
            user.clear()

        return {"status": "success", "data": user_list}, 200

    def post(self):
        json_data = request.get_json()

        if not json_data:
            return {"message": "No input data provided"}, 400

        uui = Re.uuid()
        user = Re.checkUser(json_data["username"])
        email = Re.checkEmail(json_data["email"])
        key = KEY.password()
        api_key = Re.encrypt_key()

        if user:
            return {"message": "Username not available"}, 400

        if email:
            return {"message": "emailadress already listed"}, 400

        password = json_data["password"].encode()
        first_name = json_data["first_name"].encode()
        last_name = json_data["last_name"].encode()

        user = Users(
            uuid=uui,
            username=json_data["username"],
            password=Encryption.encoder(password, key).decode(),
            email=json_data["email"],
            first_name=Encryption.encoder(first_name, key).decode(),
            last_name=Encryption.encoder(last_name, key).decode(),
            encryption_key=key,
            api_key=api_key,
        )
        db.session.add(user)
        db.session.commit()

        result = Users.serialize(user)

        return {"status": "success", "data": result}
