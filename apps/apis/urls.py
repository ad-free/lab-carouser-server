"""lab_carouser_server URL Configuration"""
from django.urls import path, include
from .router import v1

urlpatterns = [
    path('', include(v1.router.urls)),
]
