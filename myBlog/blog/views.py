from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import *

# Create your views here.


def login(request):
    """
    用户登陆界面
    :param request:
    :return:
    """
    if request.method == "GET":
        form = forms.UserForm()
        return render(request, 'blog/login.html', context={'form': form})

    elif request.method == "POST":
        request.session['account'] = request.POST.get('account')
        return redirect('/blog/1')


def index(request, page):
    """
    系统主页
    :param request:
    :return:
    """
    page = int(page)
    # 获取所有文章
    count = Article.manager.all().count()
    tags = ArticleTag.manager.all()
    kinds = ArticleKind.manager.all()
    new_articles = Article.manager.all().order_by('-publish_time')[:3]
    if count <= 10:
        articles = Article.manager.all()
        return render(request, 'blog/index.html', context={'articles': articles, 'tags': tags, 'kinds': kinds, 'new_articles': new_articles})
    else:
        page_count = count//10 + 1
        if page > page_count:
            return HttpResponse('该页面不存在')
        else:
            articles = Article.manager.all()[(page-1)*10:page*10]
            pages = [x+1 for x in range(page_count)]
            return render(request, 'blog/index.html', context={'articles': articles, 'tags': tags, 'kinds': kinds,
                                                               'pages': pages, 'current_page': page, 'new_articles': new_articles})
