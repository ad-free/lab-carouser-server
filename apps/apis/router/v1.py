"""lab_carouser_server URL Configuration"""
from rest_framework import routers

from apps.apis.views import api_login, api_logout, api_register, \
    api_profile_detail, api_profile_update, api_city_list, \
    api_friend_add, api_user_list, api_friend_list, api_friend_remove

router = routers.DefaultRouter()
router.register('register', api_register.Register, basename='register')
router.register('login', api_login.Login, basename='login')
router.register('logout', api_logout.Logout, basename='logout')
router.register('users', api_user_list.UserList, basename='user-list')
router.register('profile/update', api_profile_update.ProfileUpdate, basename='profile-update')
router.register('profile/detail', api_profile_detail.ProfileDetail, basename='profile-detail')
router.register('friends', api_friend_list.FriendList, basename='friend-list')
router.register('friends/add', api_friend_add.AddFriend, basename='friend-add')
router.register('friends/remove', api_friend_remove.RemoveFriend, basename='friend-remove')
router.register('cities', api_city_list.CityList, basename='city-list')
