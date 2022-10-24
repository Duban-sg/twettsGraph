from dataclasses import fields
from rest_framework import serializers
from authApp.models.followers import Followers

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = ['id', 'screen_name_base', 'date']