
from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    print(request)
    # 加载模板
    template = loader.get_template("booktest/index.html")
    # 构造上下文
    content = {}
    # 渲染模板
    result = template.render(context=content)
    # 将模板发送至浏览器
    return HttpResponse(result)
    # return HttpResponse("show index")


def detail(request, id):
    book = Goods.objects.get(pk=id)
    return render(request, "booktest/detail.html", {"book": book})


def book_list(request):
    # 加载模板
    # template = loader.get_template('booktest/list.html')

    booklist = Goods.objects.all()
    # # 构造上下文
    context = {"booklist": booklist}
    # # 渲染模板
    # result = template.render(context=context)
    # return HttpResponse(result)
    # # return HttpResponse("list" )

    # 简写操作
    return render(request, 'booktest/list.html', context)