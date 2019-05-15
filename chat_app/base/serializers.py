from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_delete', 'password') # 表示在序列化的时候不会返回password、is_delete字段

class UserFriendSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    friend = UserSerializer() # 将外键也序列化成json返回
    class Meta:
        model = UserFriends
        exclude = ('is_delete',)