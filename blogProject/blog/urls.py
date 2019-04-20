from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = "blog"

urlpatterns = [
    # 注册主页地址
    url(r'^$', views.index, name="index"),
    url(r'login_register$', views.login_register, name="login_register"),
    url(r'login$', views.login, name="login"),
    url(r'register$', views.register, name="register"),
    url(r'home$', views.home, name="home"),
    url(r'publish$', views.publish_article, name="publish"),
    url(r'manage_article$', views.manage_article, name="manage_article"),
    url(r'update_article$', views.update_article, name="update_article"),
    # url(r'detail/(%d+)$', views.look_article, name="detail"),
    url(r'detail/.*', views.detail_article, name="detail"),
    url(r'delete/.*', views.del_article, name="delete"),
    url(r'comment/.*', views.comment_article, name="comment"),
]
