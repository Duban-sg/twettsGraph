
from django.urls import include, path
from rest_framework import routers
from authApp import views

router = routers.DefaultRouter()
router.register(r'tweets', views.TweetsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
