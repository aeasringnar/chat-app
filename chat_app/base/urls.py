from django.conf.urls import url
from base import views

urlpatterns = [
    url(r'^login$',views.Login.as_view(),name='login'),
    url(r'^register$',views.Register.as_view(),name='register'),
    url(r'^userinfo$',views.UserInfo.as_view(),name='userinfo'),
    url(r'^logout$',views.Logout.as_view(),name='logout'),
    url(r'^userfriends$',views.UserFriendList.as_view(),name='userfriend'),
    url(r'^friendinfo$',views.FriendInfo.as_view(),name='friendinfo'),
    url(r'^addfriend$',views.AddFriend.as_view(),name='addfriend'),
    url(r'^findfriend$',views.FindFriend.as_view(),name='findfriend'),
]