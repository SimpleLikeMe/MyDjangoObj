from django.conf.urls import url
from . import views

app_name = 'shopping'

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^home/([1-4])/$', views.home, name='home'),
    url('^blog/$', views.blog, name='blog'),
    url('^blog_details/$', views.blog_details, name='blog_details'),
    url('^contact/$', views.contact, name='contact'),
    url('^shop_grid/$', views.shop_grid, name='shop_grid'),
]



