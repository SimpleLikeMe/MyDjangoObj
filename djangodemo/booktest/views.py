
from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    # 加载模板
    # template = loader.get_template("templates/index.html")
    # 构造上下文
    content = {}
    # 渲染模板
    # result = template.render(context=None)
    # 将模板发送至浏览器
    # return HttpResponse(result)
    return HttpResponse("index")


def detail(request, id):
    return HttpResponse("detail %s" % (id,))


def book_list(request, id):
    return HttpResponse("detail %s" % (id,))
