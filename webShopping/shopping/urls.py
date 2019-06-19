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
    url('^product_details/$', views.product_details, name='product_details'),
    url('^about/$', views.about, name='about'),
    url('^account/$', views.account, name='account'),
    url('^wishlist/$', views.wishlist, name='wishlist'),
    url('^shop_list/$', views.shop_list, name='shop_list'),
    url('^cart/$', views.cart, name='cart'),
    url('^checkout/$', views.checkout, name='checkout'),
    url('^page404/$', views.page404, name='page404'),
]



