from django.shortcuts import render, redirect
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
        return redirect('/blog')


def index(request, page):
    """
    系统主页
    :param request:
    :return:
    """
    print(page)
    # 获取所有文章
    articles = Article.manager.all()
    return render(request, 'blog/index.html', context={'articles': articles})
