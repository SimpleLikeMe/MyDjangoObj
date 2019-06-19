from django.conf.urls import url
from . import views

app_name = 'shopping'

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^([1-4])/$', views.home, name='home'),
    url('^blog/$', views.blog, name='blog'),
]



