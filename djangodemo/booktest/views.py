
from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    print(request)
    # 加载模板
    template = loader.get_template("index.html")
    # 构造上下文
    content = {}
    # 渲染模板
    result = template.render(context=content)
    # 将模板发送至浏览器
    return HttpResponse(result)
    # return HttpResponse("show index")


def detail(request, id):
    return HttpResponse("detail %s" % (id,))


def book_list(request):
    # 加载模板
    template = loader.get_template('list.html')
    booklist = Goods.objects.all()
    # 构造上下文
    context = {"booklist": booklist}
    # 渲染模板
    result = template.render(context=context)
    return HttpResponse(result)
    # return HttpResponse("list" )
