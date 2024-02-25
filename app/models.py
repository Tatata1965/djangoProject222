from django.db import models
from django.db.models import CharField, DateField


# Create your models here.
class Users(models.Model):
    login = CharField(max_length=10)
    password = CharField(max_length=10)
    birthday = DateField(null=True)
