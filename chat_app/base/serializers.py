from rest_framework import serializers
from .models import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name','zhname')

class UserSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    class Meta:
        model = User
        fields = ('id','nickname','user_account','phone','user_status','email','gender','password','birthday','info','addr','qq','weixin','group','image_url')

class UserFriendSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    friend = UserSerializer()
    class Meta:
        model = UserFriends
        fields = ('id','user','friend')

