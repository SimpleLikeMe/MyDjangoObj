from django import template
from ..models import *

# 得到django负责管理标签和过滤器类
register = template.Library()


@register.filter(name='mylower')
def mylower(value):
    """
    添加转小写方法
    :param value: 应用过滤器的对象
    :return:
    """
    return value.lower()


@register.filter(name="myjoin")
def myjoin(value, sep):
    return value.join(sep)


@register.simple_tag
def getArticleMonth():
    return Article.manager.all().dates('publish_time', 'month', order='DESC')[:6]


@register.simple_tag
def getKindArticles(kind):
    return Article.manager.all().filter(kind=kind)

