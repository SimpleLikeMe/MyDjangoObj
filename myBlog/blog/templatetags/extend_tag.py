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



@register.simple_tag
def getArticleMonth():
    return Article.manager.all().dates('publish_time', 'month', order='DESC')[:6]


@register.simple_tag
def getArticleKind():
    return ArticleKind.manager.all()


@register.simple_tag
def getNewArticles():
    articles = Article.manager.all()
    if articles.count() <= 3:
        return articles
    else:
        return articles[:3]


@register.simple_tag
def getArticleTag():
    return ArticleTag.manager.all()

