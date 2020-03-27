from django.conf.urls import url

from django.urls import path, include




urlpatterns = [
    path('drf/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('doc.api_urls', namespace='api')),
]
