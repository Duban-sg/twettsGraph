from django.db.models import Model, UUIDField, CharField, EmailField, DateTimeField
from django.db import models

class Tweets(models.Model):
    id = UUIDField(primary_key=True)
    geo = CharField(max_length=155)