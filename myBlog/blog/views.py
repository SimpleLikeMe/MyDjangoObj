from django.shortcuts import render, redirect
from comment.forms import CommentForm
from comment.models import CommentManager
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
    if count <= 3:
        articles = Article.manager.all()
        return render(request, 'blog/index.html', context={'articles': articles})
    else:
        page_count = count//3 + 1
        if page > page_count:
            return HttpResponse('该页面不存在')
        else:
            articles = Article.manager.all()[(page-1)*3:page*3]
            pages = [x+1 for x in range(page_count)]
            return render(request, 'blog/index.html', context={'articles': articles, 'pages': pages, 'current_page': page})


def full_width(request, page):
    page = int(page)
    count = Article.manager.all().count()
    if count <= 10:
        articles = Article.manager.all()
        return render(request, 'blog/full-width.html',
                      context={'articles': articles})
    else:
        page_count = count // 10 + 1
        if page > page_count:
            return HttpResponse('该页面不存在')
        else:
            articles = Article.manager.all()[(page - 1) * 10:page * 10]
            pages = [x + 1 for x in range(page_count)]
            return render(request, 'blog/full-width.html', context={'articles': articles})


def single(request, aid):
    article = Article.manager.all().filter(pk=aid).first()
    if request.method == "GET":
        form = CommentForm()
        article.read_count += 1
        article.save()
        return render(request, 'blog/single.html', context={'article': article, 'form': form})
    elif request.method == "POST":
        return render(request, 'blog/single.html', context={'article': article})


def comment(request, aid):
    """
    评论处理
    :param request:
    :return:
    """
    article = Article.manager.all().filter(pk=aid).first()
    if request.method == "GET":
        form = CommentForm()
        article.read_count += 1
        return render(request, 'blog/single.html', context={'article': article, 'form': form})
    elif request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.user = User.manager.all().filter(account=request.session.get("account")).first()
            comment.article = Article.manager.all().filter(pk=aid).first()
            comment.article.comment_count += 1
            comment.article.save()
            comment.save()
            return redirect('/blog/single/%s' % aid)
        else:
            return HttpResponse("该页面不存在")


def article_kind(request, page, kid):
    """
    文章分类
    :param request:
    :param page:
    :param kind:
    :return:
    """
    page = int(page)
    # 获取所有文章
    count = Article.manager.all().filter(kind=kid).count()
    tags = ArticleTag.manager.all()
    kinds = ArticleKind.manager.all()
    new_articles = Article.manager.all().order_by('-publish_time')[:3]
    if count <= 3:
        articles = Article.manager.all().filter(kind=kid)
        return render(request, 'blog/index.html', context={'articles': articles, 'tags': tags, 'kinds': kinds, 'new_articles': new_articles})
    else:
        page_count = count//3 + 1
        if page > page_count:
            return HttpResponse('该页面不存在')
        else:
            articles = Article.manager.all().filter(kind=kid)[(page-1)*3:page*3]
            pages = [x+1 for x in range(page_count)]
            return render(request, 'blog/index.html', context={'articles': articles, 'tags': tags, 'kinds': kinds,
                                                               'pages': pages, 'current_page': page, 'new_articles': new_articles})


def article_tag(request, page, tid):
    """
    文章分类
    :param request:
    :param page:
    :param kind:
    :return:
    """
    page = int(page)
    # 获取所有文章
    count = ArticleTag.manager.all().filter(kp=tid).first().article.all().count()
    tags = ArticleTag.manager.all()
    kinds = ArticleKind.manager.all()
    new_articles = Article.manager.all().order_by('-publish_time')[:3]
    if count <= 3:
        articles = ArticleTag.manager.all().filter(kp=tid).first().article.all()
        return render(request, 'blog/index.html', context={'articles': articles, 'tags': tags, 'kinds': kinds, 'new_articles': new_articles})
    else:
        page_count = count//3 + 1
        if page > page_count:
            return HttpResponse('该页面不存在')
        else:
            articles = ArticleTag.manager.all().filter(kp=tid).first().article.all()[(page-1)*3:page*3]
            pages = [x+1 for x in range(page_count)]
            return render(request, 'blog/index.html', context={'articles': articles, 'tags': tags, 'kinds': kinds,
                                                               'pages': pages, 'current_page': page, 'new_articles': new_articles})


def article_date(request, page, date):
    page = int(page)
    # 获取所有文章

    count = Article.manager.all().filter(publish_date=date).first().article.all().count()
    tags = ArticleTag.manager.all()
    kinds = ArticleKind.manager.all()
    new_articles = Article.manager.all().order_by('-publish_time')[:3]
    if count <= 3:
        articles = ArticleTag.manager.all().filter(publish_date=date).first().article.all()
        return render(request, 'blog/index.html', context={'articles': articles, 'tags': tags, 'kinds': kinds, 'new_articles': new_articles})
    else:
        page_count = count//3 + 1
        if page > page_count:
            return HttpResponse('该页面不存在')
        else:
            articles = ArticleTag.manager.all().filter(publish_date=date).first().article.all()[(page-1)*3:page*3]
            pages = [x+1 for x in range(page_count)]
            return render(request, 'blog/index.html', context={'articles': articles, 'tags': tags, 'kinds': kinds,
                                                               'pages': pages, 'current_page': page, 'new_articles': new_articles})



