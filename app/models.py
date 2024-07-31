from peewee import Model, CharField, ForeignKeyField

from app.database import db


class BaseModel(Model):
    class Meta:
        database = db


class ApiUser(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()


class Location(BaseModel):
    name = CharField()


class Device(BaseModel):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref="loc_devices")
    api_user = ForeignKeyField(ApiUser, backref="user_devices")
