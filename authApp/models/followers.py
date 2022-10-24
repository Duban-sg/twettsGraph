from django.db.models import Model, AutoField, CharField, EmailField, DateTimeField
from django.db import models


class Followers(models.Model):
    id = AutoField(primary_key=True)
    screen_name_base = CharField(max_length=155)
    date = DateTimeField()
    

    