from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.TextField()
    email = fields.TextField()
    password = fields.TextField()