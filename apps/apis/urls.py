"""lab_carouser_server URL Configuration"""
from django.urls import path, include

from rest_framework import routers

from apps.apis.views import api_login, api_logout, api_register, \
	api_profile_detail, api_profile_update, api_city_list, \
	api_friend_add, api_user_list, api_friend_list, api_friend_remove
<<<<<<< HEAD

router = routers.DefaultRouter()
router.register('register', api_register.Register, base_name='register')
router.register('login', api_login.Login, base_name='login')
router.register('logout', api_logout.Logout, base_name='logout')
router.register('users', api_user_list.UserList, base_name='user-list')
router.register('profile/update', api_profile_update.ProfileUpdate, base_name='profile-update')
router.register('profile/detail', api_profile_detail.ProfileDetail, base_name='profile-detail')
router.register('friends', api_friend_list.FriendList, base_name='friend-list')
router.register('friends/add', api_friend_add.AddFriend, base_name='friend-add')
router.register('friends/remove', api_friend_remove.RemoveFriend, base_name='friend-remove')
router.register('cities', api_city_list.CityList, base_name='city-list')


urlpatterns = [
	path('', include(router.urls)),
=======

router = routers.DefaultRouter()
router.register('register', api_register.Register, base_name='register')
router.register('login', api_login.Login, base_name='login')
router.register('logout', api_logout.Logout, base_name='logout')
router.register('users', api_user_list.UserList, base_name='user-list')
router.register('profile/update', api_profile_update.ProfileUpdate, base_name='profile-update')
router.register('profile/detail', api_profile_detail.ProfileDetail, base_name='profile-detail')
router.register('friends', api_friend_list.FriendList, base_name='friend-list')
router.register('friends/add', api_friend_add.AddFriend, base_name='friend-add')
router.register('friends/remove', api_friend_remove.RemoveFriend, base_name='friend-remove')
router.register('cities', api_city_list.CityList, base_name='city-list')


urlpatterns = [
<<<<<<< HEAD
	path('register/', api_register.Register.as_view(), name='api_auth_register'),
	path('login/', api_login.Login.as_view(), name='api_auth_login'),
	path('logout/', api_logout.Logout.as_view(), name='api_auth_logout'),
	path('profile/update/', api_profile_update.ProfileUpdate.as_view(), name='api_profile_update'),
	path('profile/detail/', api_profile_detail.ProfileDetail.as_view(), name='api_profile_detail'),
	path('user/list/', api_user_list.UserList.as_view(), name='api_user_list'),
	path('friend/add/', api_friend_add.AddFriend.as_view(), name='api_friend_add'),
	path('friend/list/', api_friend_list.FriendList.as_view(), name='api_friend_list'),
	path('friend/remove/', api_friend_remove.RemoveFriend.as_view(), name='api_friend_remove'),
	path('city/list/', api_city_list.CityList.as_view(), name='api_City_list'),
>>>>>>> e164e79... Update and optimize
=======
	path('', include(router.urls)),
>>>>>>> 40ba4e0... Update README.md
]
