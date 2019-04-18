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
    # 是否激活
    # is_Delete = models.BooleanField()

    def __str__(self):
        return self.account

    def show_account(self):
        return self.account
    show_account.short_description = "账号"

    def show_nickname(self):
        return self.nickname
    show_nickname.short_description = "昵称"

    def show_email(self):
        return self.email
    show_email.short_description = "邮箱"

    def show_integral(self):
        return self.integral
    show_integral.short_description = "积分"

    def show_register_time(self):
        return self.register_time
    show_register_time.short_description = "注册时间"


class Article(models.Model):
    """
        构建文章对象
    """
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    read_count = models.IntegerField(default=0)
    publish_time = models.DateTimeField(auto_now_add=True)

    def show_title(self):
        return self.title
    show_title.short_description = "标题"

    # def show_id(self):
    #     return self.id
    # show_id.short_description = "邮箱"

    def show_read_count(self):
        return self.read_count
    show_read_count.short_description = "浏览次数"

    def show_publish_time(self):
        return self.publish_time
    show_publish_time.short_description = "发布时间"

    def __str__(self):
        return self.title











