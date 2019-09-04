"""lab_carouser_server URL Configuration"""
from django.urls import path

from apps.apis.views import api_login, api_logout, api_register, \
	api_profile_detail, api_profile_update, api_location_list

urlpatterns = [
	path('register/', api_register.Register.as_view()),
	path('login/', api_login.Login.as_view()),
	path('logout/', api_logout.Logout.as_view()),
	path('profile/update/', api_profile_update.ProfileUpdate.as_view()),
	path('profile/detail/', api_profile_detail.ProfileDetail.as_view()),
	path('location/list/', api_location_list.LocationList.as_view()),
]
