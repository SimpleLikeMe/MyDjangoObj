from django.db import models

# Create your models here.


class User(models.Model):
    """
        创建用户表，继承model下的Model类，该类提供了与数据库交互的所有方法
    """

    # 构建字段,用户账号
    account = models.CharField(max_length=20, unique=True)
    # 用户密码
    password = models.CharField(max_length=30)
    # 用户昵称
    nickname = models.CharField(max_length=20, blank=True, default="新用户")
    # 用户邮箱
    email = models.CharField(max_length=30, blank=True, default="待完善")
    # 用户积分
    integral = models.IntegerField(default=10)
    # 用户说明
    describe = models.CharField(max_length=255, blank=True, default="暂无说明")
    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    """
        构建文章对象
    """
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    read_count = models.IntegerField(default=0)
    publish_time = models.DateTimeField(auto_now_add=True)











