
from django.urls import include, path
from rest_framework import routers
from authApp.views import TweetsViewSet

router = routers.DefaultRouter()
router.register(r'tweets', TweetsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
