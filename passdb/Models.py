from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql.base import MSBinary


ma = Marshmallow()
db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = tuple(
        db.UniqueConstraint("id", "username", "email", "encryption_key", "api_key")
    )

    uuid = db.Column(db.String(300), name="id", primary_key=True, unique=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(400), unique=True)
    encryption_key = db.Column(db.String(160), unique=True)
    api_key = db.Column(db.String(500), unique=True)
    first_name = db.Column(db.String(500))
    last_name = db.Column(db.String(500))
    password = db.Column(db.String(500))

    def __init__(
        self,
        username,
        first_name,
        last_name,
        password,
        email,
        encryption_key,
        api_key,
        uuid,
    ):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.encryption_key = encryption_key
        self.api_key = api_key
        self.uuid = uuid

    def __repr__(self):
        return "<id {}>".format(self.uuid)

    def serialize(self):
        return {
            "id": self.uuid,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "email": self.email,
            "encryption_key": self.encryption_key,
            "api_key": self.api_key,
        }

    def normal(self):
        return {
            "id": self.uuid,
            "username": self.username,
            "email": self.email,
            "api_key": self.api_key,
            "encryption_key": self.encryption_key,
        }

    def encoded(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
        }

    def key(self):
        return {
            "encryption_key": self.encryption_key,
        }


class Content(db.Model):

    __tablename__ = "Content"
    __table_args__ = tuple(
        db.UniqueConstraint("Uid", "username", "passWord", "webPage", "link")
    )

    uuid = db.Column(db.String(300), name="id", primary_key=True, unique=True)
    username = db.Column(db.String(150))
    passWord = db.Column(db.String(400))
    webPage = db.Column(db.String(160))
    link = db.Column(db.String(5000))

    def __init__(
        self,
        username,
        passWord,
        webPage,
        link,
        uuid,
    ):
        self.username = username
        self.link = link
        self.webPage = webPage
        self.passWord = passWord
        self.uuid = uuid

    def serialize(self):
        return {
            "id": self.uuid,
            "username": self.username,
            "link": self.link,
            "webPage": self.webPage,
            "password": self.passWord,
        }

    def normal(self):
        return {
            "webPage": self.webPage,
            "link": self.link,
        }

    def encoded(self):
        return {
            "password": self.passWord,
        }
