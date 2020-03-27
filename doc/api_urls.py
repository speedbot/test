from rest_framework import routers
from . import views
from django.urls import include
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'document', views.DocumentViewSet)

app_name = 'api'

urlpatterns = [
    url(r'^', include(router.urls)),
]