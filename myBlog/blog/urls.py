from django.conf.urls import url, include
from . import views

# 设置应用命名空间
app_name = 'blog'


# 配置应用url
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^login/$', views.login, name='login'),
    url('^(\d+)/$', views.index, name='index'),
    url('^full_width/(\d+)/$', views.full_width, name='full_width'),
    url('^single/(\d+)/$', views.single, name='single'),
    url('^comment/(\d+)/$', views.comment, name='comment'),
    url('^kind/(\d+)/(\d+)/$', views.article_kind, name='article_kind'),
    url('^tag/(\d+)/(\d+)/$', views.article_tag, name='article_tag'),
    url('^file/(\d+)/(\d{4})/(\d{1})/$', views.article_date, name='article_date'),
]
