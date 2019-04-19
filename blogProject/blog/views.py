from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.


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
        try:
            account = request.POST["account"]
            pwd = request.POST["password"]
            user = User.objects.get(account=account)
            if user.password == pwd:
                articles = Article.objects.all()
                return render(request, 'blog/home.html', context={"articles": articles})
            else:
                return HttpResponseRedirect('/blog/login')
        except:
            return HttpResponseRedirect('/blog/login')


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

        try:
            if User.objects.get(account=account):
                return HttpResponseRedirect('/blog/register')
        except:
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
    account = request.POST["account"]
    pwd = request.POST["password"]
    try:
        if User.objects.get(account=account).password == pwd:
            return render(request, 'blog/home.html')
        else:
            return HttpResponseRedirect('blog/login')
    except:
        return HttpResponseRedirect('blog/login')


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
    print("发表文章")
    title = request.POST["title"]
    content = request.POST["content"]
    article = Article()
    article.title = title
    article.content = content
    article.save()
    articles = Article.objects.all()

    return render(request, "blog/home.html", context={"articles": articles})




