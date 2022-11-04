from django.db import models
from django.db.models import (AutoField, CharField, DateTimeField, EmailField,
                              Model)


class Followers(models.Model):
    id = AutoField(primary_key=True)
    screen_name_base = CharField(max_length=155)
    date = DateTimeField()
    

    