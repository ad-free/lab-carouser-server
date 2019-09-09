"""lab_carouser_server URL Configuration"""
from django.urls import path

from apps.apis.views import api_login, api_logout, api_register, \
	api_profile_detail, api_profile_update, api_location_list, \
	api_friend_add, api_friend_list, api_friend_accept, \
	api_friend_accept_list, api_friend_remove, api_friend_anonymous

urlpatterns = [
	path('register/', api_register.Register.as_view(), name='api_auth_register'),
	path('login/', api_login.Login.as_view(), name='api_auth_login'),
	path('logout/', api_logout.Logout.as_view(), name='api_auth_logout'),
	path('profile/update/', api_profile_update.ProfileUpdate.as_view(), name='api_profile_update'),
	path('profile/detail/', api_profile_detail.ProfileDetail.as_view(), name='api_profile_detail'),
	path('friend/add/', api_friend_add.AddFriend.as_view(), name='api_friend_add'),
	path('friend/list/', api_friend_list.ListFriend.as_view(), name='api_friend_list'),
	path('friend/anonymous/', api_friend_anonymous.AnonymousFriend.as_view(), name='api_friend_anonymous'),
	path('friend/accept/', api_friend_accept.AcceptFriend.as_view(), name='api_friend_accept'),
	path('friend/accept/list/', api_friend_accept_list.AcceptList.as_view(), name='api_friend_accept_list'),
	path('friend/remove/', api_friend_remove.RemoveFriend.as_view(), name='api_friend_remove'),
	path('location/list/', api_location_list.LocationList.as_view(), name='api_location_list'),
]
