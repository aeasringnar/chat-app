import re
from django.db.models import Q
from rest_framework import serializers, status, generics
# 使用APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime,time,random
# 缓存配置
from django.core.cache import cache
# JWT配置
from .utils import jwt_payload_handler, jwt_encode_handler,google_otp,request_log
from .authentication import JWTAuthentication
from .models import *
from .serializers import *
import uuid,os,requests, json




# 登录视图
class LoginInfoSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
class Login(generics.GenericAPIView):
    serializer_class = LoginInfoSerializer
    def post(self,request):
        request_log(request)
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({"message": str(serializer.errors), "errorCode": 4, "data": {}})
            data = (serializer.data)
            username = data.get('username')
            password = data.get('password')
            user = User.objects.filter(Q(phone=username) | Q(user_account=username) | Q(nickname=username), is_delete=False).first()
            if not user:
                return Response({"message": "用户不存在", "errorCode": 2, "data": {}})
            if user.password == password:
                user.user_status = 1
                user.save()
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({"message": "登录成功", "errorCode": 0, "data": {'token':token}})
            else:
                return Response({"message": "密码错误", "errorCode": 0, "data": {}})
        except Exception as e:
            print(e)
            return Response({"message": "未知错误", "errorCode": 1, "data": {}})


# 获取用户账号的方法
def get_chat_account():
    import random
    first_num = random.choice(['1','2','3','4','5','6','7','8','9'])
    end_num = [str(random.randint(0,9)) for _ in range(3)]
    account = first_num + ''.join(end_num)
    return account


# 注册视图
class UserRegisterSerializer(serializers.Serializer):
    nickname = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()
class Register(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self,request):
        request_log(request)
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({"message": str(serializer.errors), "errorCode": 4, "data": {}})
            data = (serializer.data)
            nickname = data.get('nickname')
            password = data.get('password')
            phone = data.get('phone')
            phone_re = re.compile(r'^1(3[0-9]|4[57]|5[0-35-9]|7[0135678]|8[0-9])\d{8}$', re.IGNORECASE)
            if not phone_re.match(phone):
                return Response({"message": "手机号格式错误", "errorCode": 2, "data": {}})

            user_account = get_chat_account()
            print(user_account)
            while True:
                account_check = User.objects.filter(user_account=user_account, is_delete=False)
                if account_check:
                    user_account = get_chat_account()
                else:
                    break
            print(user_account)
            phone_check = User.objects.filter(phone=phone, is_delete=False)
            if phone_check:
                return Response({"message": "手机号已经存在", "errorCode": 2})
            account = User()
            account.phone = phone
            account.user_account = user_account
            # 明文密码
            account.password = password
            account.nickname = nickname
            account.save()
            return Response({"message": "ok", "errorCode": 0, "data": {"user_account":user_account}})
        except Exception as e:
            print(e)
            return Response({"message": "未知错误", "errorCode": 1, "data": {}})


# 获取用户信息视图
class UserInfo(APIView):
    authentication_classes = (JWTAuthentication,)
    def get(self,request):
        request_log(request)
        try:
            if not request.auth:
                return Response({"message": "请先登录", "errorCode": 2, "data": {}})
            user = User.objects.filter(id=request.user.id,is_delete=False).first()
            serializer_user_data = UserSerializer(user)
            json_data = {"message": "ok", "errorCode": 0, "data": {}}
            json_data['data'] = serializer_user_data.data
            return Response(json_data)
        except Exception as e:
            print(e)
            return Response({"message": "未知错误", "errorCode": 1, "data": {}})


# 获取好友用户信息视图
class FriendInfo(APIView):
    authentication_classes = (JWTAuthentication,)
    def get(self,request):
        request_log(request)
        try:
            if not request.auth:
                return Response({"message": "请先登录", "errorCode": 2, "data": {}})
            json_data = {"message": "ok", "errorCode": 0, "data": {}}
            friend_id = request.GET.get('friend_id')
            if not friend_id:
                return Response({"message": "请传入friend_id", "errorCode": 2, "data": {}})
            friend = User.objects.filter(id=int(friend_id),is_delete=False).first()
            if not friend:
                return Response({"message": "用户不存在或已删除", "errorCode": 2, "data": {}})
            serializer_friend_data = UserSerializer(friend)
            json_data['data'] = serializer_friend_data.data
            return Response(json_data)
        except Exception as e:
            print(e)
            return Response({"message": "未知错误", "errorCode": 1, "data": {}})


# 用户退出登录视图
class Logout(APIView):
    authentication_classes = (JWTAuthentication,)
    def get(self,request):
        request_log(request)
        try:
            if not request.auth:
                return Response({"message": "请先登录", "errorCode": 2, "data": {}})
            user = User.objects.filter(id=request.user.id,is_delete=False).first()
            user.user_status = 0
            user.save()
            json_data = {"message": "ok", "errorCode": 0, "data": {}}
            return Response(json_data)
        except Exception as e:
            print(e)
            return Response({"message": "未知错误", "errorCode": 1, "data": {}})


# 获取好友列表视图
class UserFriendList(APIView):
    authentication_classes = (JWTAuthentication,)
    def get(self,request):
        request_log(request)
        try:
            if not request.auth:
                return Response({"message": "请先登录", "errorCode": 2, "data": {}})
            json_data = {"message": "ok", "errorCode": 0, "data": {}}
            user_friends = UserFriends.objects.filter(user_id=request.user.id,is_delete=False)
            serializer_user_friends_data = UserFriendSerializer(user_friends,many=True)
            json_data['data'] = serializer_user_friends_data.data
            return Response(json_data)
        except Exception as e:
            print(e)
            return Response({"message": "未知错误", "errorCode": 1, "data": {}})


# 添加好友视图
class AddFriendSerializer(serializers.Serializer):
    friend_id = serializers.IntegerField()
class AddFriend(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    serializer_class = AddFriendSerializer
    def post(self,request):
        request_log(request)
        try:
            if not request.auth:
                return Response({"message": "请先登录", "errorCode": 2, "data": {}})
            json_data = {"message": "ok", "errorCode": 0, "data": {}}
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({"message": str(serializer.errors), "errorCode": 4, "data": {}})
            data = (serializer.data)
            friend_id = data.get('friend_id')
            friend = User.objects.filter(id=int(friend_id),is_delete=False).first()
            if not friend:
                return Response({"message": "用户不存在或已删除", "errorCode": 2, "data": {}})
            # 将别人确认加为我的好友
            user_friend = UserFriends()
            user_friend.user_id = request.user.id
            user_friend.friend_id = friend_id
            user_friend.save()
            # 将对方的的好友列表中加入我
            friend_user = UserFriends()
            friend_user.user_id = friend_id
            friend_user.friend_id = request.user.id
            friend_user.save()
            return Response(json_data)
        except Exception as e:
            print(e)
            return Response({"message": "未知错误", "errorCode": 1, "data": {}})


# 搜索好友视图
class FindFriend(APIView):
    authentication_classes = (JWTAuthentication,)
    def get(self,request):
        request_log(request)
        try:
            if not request.auth:
                return Response({"message": "请先登录", "errorCode": 2, "data": {}})
            json_data = {"message": "ok", "errorCode": 0, "data": {}}
            keyword = request.GET.get('keyword')
            if not keyword:
                return Response({"message": "请传入keyword", "errorCode": 2, "data": {}})
            friend = User.objects.filter(Q(phone__contains=keyword) | Q(user_account__contains=keyword) | Q(nickname__contains=keyword),is_delete=False)
            if not friend:
                return Response({"message": "用户不存在或已删除", "errorCode": 2, "data": {}})
            serializer_friend_data = UserSerializer(friend,many=True)
            json_data['data'] = serializer_friend_data.data
            return Response(json_data)
        except Exception as e:
            print(e)
            return Response({"message": "未知错误", "errorCode": 1, "data": {}})