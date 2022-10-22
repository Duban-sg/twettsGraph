
from authApp.models.tweets import Tweets
from rest_framework import viewsets
from authApp.serializers.tweetSerializer import TweetsSerializer

class TweetsViewSet(viewsets.ModelViewSet):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer
