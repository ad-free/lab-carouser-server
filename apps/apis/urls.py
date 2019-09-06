"""lab_carouser_server URL Configuration"""
from django.urls import path

from apps.apis.views import api_login, api_logout, api_register, \
	api_profile_detail, api_profile_update, api_location_list

urlpatterns = [
	path('register/', api_register.Register.as_view(), name='api_auth_register'),
	path('login/', api_login.Login.as_view(), name='api_auth_login'),
	path('logout/', api_logout.Logout.as_view(), name='api_auth_logout'),
	path('profile/update/', api_profile_update.ProfileUpdate.as_view(), name='api_profile_update'),
	path('profile/detail/', api_profile_detail.ProfileDetail.as_view(), name='api_profile_detail'),
	path('location/list/', api_location_list.LocationList.as_view(), name='api_location_list'),
]
