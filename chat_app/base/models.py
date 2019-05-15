from django.db import models

# 基本表
class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True

class User(BaseModel): # 继承基本表
    GENDER_CHOICES = (
        (0, '女'),
        (1, '男'),
        (2, '保密'),
        (3, '未设置'),
    )
    nickname = models.CharField(max_length=255,default='',verbose_name='昵称')
    user_account = models.CharField(max_length=12,verbose_name='用户帐号')
    phone = models.CharField(max_length=11,verbose_name='用户手机号',null=True)
    password = models.CharField(max_length=255,default='123456',verbose_name='用户密码')
    gender = models.IntegerField(default=3,choices=GENDER_CHOICES,verbose_name='用户性别',null=True)
    user_status = models.IntegerField(default=0,verbose_name='用户在线状态',null=True)
    image_url = models.FileField(upload_to='testimage/%Y%m',verbose_name='用户头像',null=True)
    birthday = models.DateField(auto_now_add=True,null=True,verbose_name='用户生日')
    info = models.TextField(null=True,verbose_name='用户信息')
    addr = models.CharField(max_length=255,null=True,verbose_name='用户地址')

    class Meta:
        db_table = 'A_User_Table'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class UserFriends(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户id',related_name='user_dict',null=True)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='好友id',related_name='friend_dict',null=True)

    class Meta:
        db_table = 'A_UserFrineds_Table'
        verbose_name = '好友列表'
        verbose_name_plural = verbose_name