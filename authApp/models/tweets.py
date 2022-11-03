from django.db import models
from django.db.models import (CharField, DateTimeField, EmailField, Model,
                              UUIDField)


class Tweets(models.Model):
    id = UUIDField(primary_key=True)
    geo = CharField(max_length=155)
    title = models.CharField(max_length=255)
    content = models.TextField() #lat,long
    #screen_name
    #favorite_count
    #create_at_twett
    #retweet_count
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/posts/{self.id}"