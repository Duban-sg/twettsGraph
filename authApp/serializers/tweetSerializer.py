from dataclasses import fields
from rest_framework import serializers
from authApp.models.tweets import Tweets

class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['id', 'geo', 'title', 'content']