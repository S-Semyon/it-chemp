from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    last_name = fields.TextField()
    email = fields.TextField()
    password = fields.TextField()