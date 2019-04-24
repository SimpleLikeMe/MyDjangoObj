from django.conf.urls import url, include
from . import views

# 设置应用命名空间
app_name = 'blog'


# 配置应用url
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^login/$', views.login, name='login'),
    url('^(\d+)/$', views.index, name='index'),
]
