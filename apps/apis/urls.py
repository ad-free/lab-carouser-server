"""lab_carouser_server URL Configuration"""
from django.urls import path

from apps.apis.views.api_login import Login
from apps.apis.views.api_logout import Logout
from apps.apis.views.api_register import Register

urlpatterns = [
	path('register', Register.as_view()),
	path('login', Login.as_view()),
	path('logout', Logout.as_view()),
	# path('profile/update/', ''),
	# path('profile/detail/', ''),
	# path('friend/add/', ''),
	# path('friend/remove/', ''),
]
