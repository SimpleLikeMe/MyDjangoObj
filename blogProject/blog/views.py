from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# 邮件类库
from django.core.mail import send_mail, send_mass_mail
from PIL import Image, ImageDraw, ImageFont
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings
import random,io
from .models import *

# Create your views here.


def serialize(request):
    # 获取序列化工具
    serutil = Serializer(settings.SECRET_KEY, 50)
    # 将字典序列化，并编码
    result = serutil.dumps({"name": '值'}).decode('utf-8')

    # 获取反序列化工具
    dserutil = Serializer(settings.SECRET_KEY, 50)
    try:
        obj = dserutil.loads(result)
        name = obj['name']
    except Exception:
        pass




def index(request):
    """
    主页处理函数
    :param request:请求对象
    :return: 主页html模板
    """
    return render(request, 'blog/index.html')


def login_register(request):
    """
    登录注册页面
    :param request:
    :return:
    """

    return render(request, 'blog/login.html')


def login(request):
    """
    用户登录界面
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'blog/login.html')

    elif request.method == "POST":
        account = request.POST["account"]
        pwd = request.POST["password"]
        verify_code = request.POST["verifycode"]
        users = User.objects.all().filter(account=account)
        if verify_code != request.session["verifycode"]:
            # 验证码错误
            return HttpResponseRedirect('/blog/login')

        if not users.exists():
            # 用户不存在
            return HttpResponseRedirect('/blog/login')

        if users.first().password != pwd:
            # 密码错误
            request.session['account'] = request.POST["account"]
            return HttpResponseRedirect('/blog/login')

        # 验证成功
        return HttpResponseRedirect('/blog/home')


def register(request):
    """
    注册处理函数
    :param request:
    :return:
    """

    if request.method == "GET":
        return render(request, 'blog/login.html')

    elif request.method == "POST":
        account = request.POST["account"]
        pwd = request.POST["password"]
        verify_code = request.POST["verifycode"]
        if verify_code != request.session["verifycode"]:
            # 验证码错误
            return HttpResponseRedirect('/blog/login')

        if User.objects.all().filter(account=account):
            return HttpResponseRedirect('/blog/register')
        else:
            u = User()
            u.account = account
            u.password = pwd
            u.save()
            return render(request, 'blog/index.html')


def home(request):
    """
    用户主页处理函数
    :param request: 请求对象
    :return: 注册页面html
    """
    account = request.session.get('account')
    articles = Article.objects.all()
    return render(request, 'blog/home.html', context={"articles": articles, "account": account})


def show_publish_article(request):
    """
    发表文章处理函数
    :param request:请求的对象
    :return:返回写博客页面
    """
    return render(request, "blog/publish.html")


def publish_article(request):
    """
    发表文章处理函数
    :param request:请求的对象
    :return:返回写博客页面
    """
    if request.method == "GET":
        return render(request, "blog/publish.html")
    elif request.method == "POST":
        account = request.session.get('account')
        user = User.objects.all().filter(account=account).first()
        title = request.POST["title"]
        content = request.POST["content"]
        article = Article()
        article.title = title
        article.content = content
        article.user = user
        article.save()
        return HttpResponseRedirect("/blog/home")


def manage_article(request):
    """
    管理文章处理函数
    :param request:请求的用户
    :return: html网页
    """
    account = request.session.get('account')
    articles = User.objects.all().filter(account=account).first().article_set.all
    return render(request, "blog/manage_article.html", context={"articles": articles})


def detail_article(request):
    """
    查看文章
    :param request:
    :return:
    """
    aid = request.GET["aid"]
    articles = Article.objects.all().filter(pk=aid)
    if articles.exists():
        article = articles.first()
        article.read_count += 1
        article.save()
        return render(request, "blog/detail.html", context={"article": article})
    else:
        return HttpResponseRedirect("/blog/home")


def update_article(request):
    """
    修改文章
    :param request:修改文章处理函数
    :return: 修改后得html
    """
    return


def del_article(request):
    """
    处理删除文章请求
    :param request:
    :return:
    """
    account = request.session.get("account")
    aid = request.GET["aid"]
    Article.objects.all().filter(pk=aid).delete()
    articles = User.objects.all().filter(account=account).first().article_set.all
    return render(request, "blog/manage_article.html", context={"articles": articles})


def comment_article(request):
    """
    评论文章处理
    :param request:
    :return:
    """
    account = request.session.get("account")
    aid = request.GET["aid"]
    c = Comment()
    c.user = User.objects.all().filter(account=account).first()
    article = Article.objects.all().filter(pk=aid).first()
    c.article = article
    c.content = request.GET['comment']
    c.save()
    article.comment_count += 1
    article.save()
    # return HttpResponseRedirect("/blog/detail/?")
    return render(request, "blog/detail.html", context={"article": article})


def send_email(request):
    """
    发送邮件
    :param request:
    :return:
    """
    return render(request, 'blog/send_email.html')


def verify(request):
    """
    验证码
    :param request:
    :return:
    """
    # 定义背景图片的背景颜色、宽、高
    bg_color = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 200
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bg_color)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 制造噪点
    for i in range(100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy=xy, fill=fill)

    # 定义验证码的被选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    rand_str = ''
    # 随机取出四个字母或数字
    for i in range(4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('arial.ttf', 23)
    # 字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制四个字
    draw.text((10, 12), rand_str[0], font=font, fill=fontcolor)
    draw.text((50, 12), rand_str[1], font=font, fill=fontcolor)
    draw.text((100, 12), rand_str[2], font=font, fill=fontcolor)
    draw.text((150, 12), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 返回session
    request.session['verifycode'] = rand_str
    # 获取io流
    f = io.BytesIO()
    # 将图片保存
    im.save(f, 'png')
    # 将图片的值发给前端页面进行渲染
    return HttpResponse(f.getvalue(), 'image/png')

