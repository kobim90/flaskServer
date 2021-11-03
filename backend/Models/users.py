from mongoengine import *


class Users(Document):
    first_name = StringField(required=True, max_length=20)
    last_name = StringField(required=True, max_length=20)
    id_number = StringField(required=True, max_length=9)
