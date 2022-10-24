from django.db.models import Model, AutoField, CharField, EmailField, DateTimeField,IntegerField
from django.db import models


class FollowerModel(models.Model):
    id = AutoField(primary_key=True)
    screem_name = CharField(max_length=155)
    follower_count = IntegerField()
    screen_name_base = CharField(max_length=155)
    

    