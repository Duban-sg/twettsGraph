
from django.urls import include, path
from rest_framework import routers
from authApp import views

router = routers.DefaultRouter()
router.register(r'tweets', views.TweetsViewSet)
router.register(r'followers', views.FollowerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
