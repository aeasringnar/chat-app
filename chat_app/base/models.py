from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255,default='',null=True,verbose_name='英文名')
    zhname = models.CharField(max_length=255,default='',null=True,verbose_name='中文名')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    created = models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'A_Group_Table'
        verbose_name = '用户组表'
        verbose_name_plural = verbose_name


class User(models.Model):
    GENDER_CHOICES = (
        (0, '女'),
        (1, '男'),
        (2, '保密'),
        (3, '未设置'),
    )
    nickname = models.CharField(max_length=255,default='',verbose_name='昵称')
    user_account = models.CharField(max_length=12,verbose_name='用户帐号')
    phone = models.CharField(max_length=11,verbose_name='用户手机号',null=True)
    email = models.EmailField(default='',verbose_name='用户邮箱',null=True)
    password = models.CharField(max_length=255,default='123456',verbose_name='用户密码')
    gender = models.IntegerField(default='2',verbose_name='用户性别',null=True)
    user_status = models.IntegerField(default='0',verbose_name='用户在线状态',null=True)
    image_url = models.FileField(upload_to='testimage/%Y%m',verbose_name='用户头像',null=True)
    birthday = models.DateField(auto_now_add=True,null=True,verbose_name='用户生日')
    info = models.TextField(null=True,verbose_name='用户信息')
    addr = models.CharField(max_length=255,null=True,verbose_name='用户地址')
    qq = models.CharField(max_length=255,null=True,verbose_name='绑定qq')
    weixin = models.CharField(max_length=255,null=True,verbose_name='绑定微信')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='用户组',null=True)
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    created = models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'A_User_Table'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class UserFriends(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户id',related_name='user_dict',null=True)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='好友id',related_name='friend_dict',null=True)
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    created = models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'A_UserFrineds_Table'
        verbose_name = '好友列表'
        verbose_name_plural = verbose_name