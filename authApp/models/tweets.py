from django.db import models
from django.db.models import (CharField, DateField, DateTimeField, EmailField,
                              IntegerField, Model, UUIDField)


class Tweets(models.Model):
    id = UUIDField(primary_key=True)
    geo = CharField(max_length=155)
    title = models.CharField(max_length=255)
    content = models.TextField()
    screen_name = CharField(max_length=150)
    favorite_count = IntegerField()
    retweet_count = IntegerField()
    create_at_twett= DateField()
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/posts/{self.id}"