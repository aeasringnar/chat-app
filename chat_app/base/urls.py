from django.conf.urls import url
from base import views

urlpatterns = [
    url(r'^login$',views.Login.as_view(),name='login'),# 登录接口
    url(r'^register$',views.Register.as_view(),name='register'),# 注册接口
    url(r'^userinfo$',views.UserInfo.as_view(),name='userinfo'),# 获取用户信息接口
    url(r'^logout$',views.Logout.as_view(),name='logout'),# 退出登录接口
    url(r'^userfriends$',views.UserFriendList.as_view(),name='userfriend'),# 获取用户列表接口
    url(r'^friendinfo$',views.FriendInfo.as_view(),name='friendinfo'),# 获取好友用户信息接口
    url(r'^addfriend$',views.AddFriend.as_view(),name='addfriend'),# 添加好友接口
    url(r'^findfriend$',views.FindFriend.as_view(),name='findfriend'),# 搜索好友接口
]