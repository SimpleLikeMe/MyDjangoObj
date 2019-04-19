from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = "blog"

urlpatterns = [
    # 注册主页地址
    url(r'^$', views.index, name="index"),
    url(r'^blog/login_register$', views.login_register, name="login_register"),
    url(r'^blog/login$', views.login, name="login"),
    url(r'^blog/register$', views.register, name="register"),
    url(r'^blog/home$', views.home, name="home"),
    url(r'^blog/publish$', views.publish_article, name="publish"),
    url(r'^blog/manage_article$', views.manage_article, name="manage_article"),
    url(r'^blog/update_article$', views.update_article, name="update_article"),
]
