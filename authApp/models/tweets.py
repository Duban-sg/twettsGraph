from django.db.models import Model, UUIDField, CharField, EmailField, DateTimeField
from django.db import models


class Tweets(models.Model):
    id = UUIDField(primary_key=True)
    geo = CharField(max_length=155)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/posts/{self.id}"