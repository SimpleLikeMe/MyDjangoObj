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
        account = request.POST["account"]
        pwd = request.POST["password"]
        users = User.objects.all().filter(account=account)
        if not users.exists():
            return HttpResponseRedirect('/blog/login')

        if users.first().password == pwd:
            request.session['account'] = request.POST["account"]
            return HttpResponseRedirect('/blog/home')

        else:
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
