from django.db import models
from django.db.models import (AutoField, CharField, DateTimeField, EmailField,
                              IntegerField, Model)


class FollowerModel(models.Model):
    id = AutoField(primary_key=True)
    screem_name = CharField(max_length=155)
    follower_count = IntegerField()
    screen_name_base = CharField(max_length=155)
    

    