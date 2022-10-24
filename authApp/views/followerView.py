from authApp.models.followers import Followers
from rest_framework import viewsets
from authApp.serializers.followerSerializer import FollowerSerializer

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Followers.objects.all()
    serializer_class = FollowerSerializer
