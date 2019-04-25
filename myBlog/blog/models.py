from django.db import models

# Create your models here.


class UserManager(models.Manager):
    """
    用户管理类
    """
    def create_user(self, account, password):
        user = self.model()
        user.account = account
        user.password = password
        return user

    def create_save_user(self, account, password):
        user = self.create(account=account, password=password)
        return user


class ArticleManager(models.Manager):
    """
    文章管理类
    """
    def create_article(self, title, content):
        article = self.model()
        article.title = title
        article.content = content
        return article

    def create_save_article(self, title, content):
        article = self.create(title=title, content=content)
        return article


class ArticleTagManager(models.Manager):
    """
    标签云管理类
    """
    def create_tag(self, name, article):
        tag = self.model()
        tag.name = name
        tag.article = article
        return tag

    def create_save_tag(self, name, article):
        return self.create(name=name, article=article)


class ArticleKindManager(models.Manager):
    """
    文章管理类
    """
    def create_kind(self, name):
        article_kind = self.model()
        article_kind.name = name
        return article_kind

    def create_save_kind(self, name):
        return self.create(name=name)


class User(models.Model):
    """
        创建用户表，继承model下的Model类，该类提供了与数据库交互的所有方法
    """

    # 构建字段,用户账号
    account = models.CharField(max_length=20, unique=True)
    # 用户密码
    password = models.CharField(max_length=30)
    # 用户昵称
    nickname = models.CharField(max_length=20, default="新用户")
    # 用户邮箱
    email = models.CharField(max_length=30, default="待完善")
    # 性别
    gender = models.BooleanField()
    # 年龄
    age = models.IntegerField(default=0)
    # 用户积分
    integral = models.IntegerField(default=100)
    # 用户说明
    describe = models.CharField(max_length=255,  default="暂无说明")
    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True)
    # 是否激活
    is_delete = models.BooleanField(default=False)
    # 用户管理类
    manager = UserManager()

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
    # 标题
    title = models.CharField(max_length=30)
    # 摘要
    abstract = models.CharField(max_length=255)
    # 内容
    content = models.TextField()
    # 阅读次数
    read_count = models.IntegerField(default=0)
    # 评论数
    comment_count = models.IntegerField(default=0)
    # 发布日期
    publish_date = models.DateField(auto_now_add=True)
    # 发布时间
    publish_time = models.DateTimeField(auto_now_add=True)
    # 修改
    modified_time = models.DateTimeField(auto_now=True)
    # 所属用户
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    # 类型
    kind = models.ForeignKey("ArticleKind", on_delete=models.CASCADE)
    manager = ArticleKindManager()

    def show_title(self):
        return self.title
    show_title.short_description = "标题"

    def show_read_count(self):
        return self.read_count
    show_read_count.short_description = "浏览次数"

    def show_publish_time(self):
        return self.publish_time
    show_publish_time.short_description = "发布时间"

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    # 标签名
    name = models.CharField(max_length=20)
    # 标签总数
    count = models.IntegerField(default=0)
    # 文章
    article = models.ManyToManyField(to="Article", null=True, blank=True)
    manager = ArticleTagManager()

    def __str__(self):
        return self.name


class ArticleKind(models.Model):
    # 文章种类名
    name = models.CharField(max_length=20)
    # 该种类文章数量
    count = models.IntegerField(default=0)
    manager = ArticleKindManager()

    def __str__(self):
        return self.name

