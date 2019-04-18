from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = "blog"

urlpatterns = [
    # 注册主页地址
    url('^$', views.index, name="index"),
    url('^login_register$', views.login_register, name="login_register"),
    url('^login$', views.login, name="login"),
    url('^register$', views.register, name="register"),
    url('^home$', views.home, name="home"),
    url('^show_publish$', views.show_publish_article, name="show_publish"),
    url('^publish$', views.publish_article, name="publish"),
]
