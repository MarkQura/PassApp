from flask_restful import Resource
from flask import request
from Models import db, Users, Content
from KEY import KEY
import uuid
from Encrytion import Encryption


class Re(Resource):
    def checkUser(username):
        user = Users.query.filter_by(username=username).first()
        if user:
            return True
        else:
            return False

    def notUser(username):
        user = Users.query.filter_by(username=username).first()
        if not user:
            return False
        else:
            return True

    def checkEmail(email):
        email = Users.query.filter_by(email=email).first()
        if email:
            return True
        else:
            return False

    def encrypt_key(length=50):
        key = KEY.password(length)
        confirm = Users.query.filter_by(encryption_key=key).first()
        while confirm:
            key = KEY.password()
            confirm = Users.query.filter_by(encryption_key=key).first()
        return key

    def uuid():
        uui = uuid.uuid4()
        user = Users.query.filter_by(uuid=uui).first()
        while user:
            uui = uuid.uuid4()
            user = Users.query.filter_by(uuid=uui).first()
        return uui

    def pas(user, pas):
        temp = pas.encode()
        user = Users.query.filter_by(username=user).one()
        key = Users.key(user).get("encryption_key", 0)
        passw = Encryption.encoder(temp, key).decode()
        return passw

    def passw(pas, key):
        pas.encode()
        passw = Encryption.encoder(pas, key).decode()
        return passw