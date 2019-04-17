from django.conf.urls import url
from . import views

app_name = "booktest"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.book_list, name='list'),
    # url(r'^detail/([0-9]+)/$', views.detail),
    url(r'^detail/([0-9]+)/$', views.detail, name='detail'),
]

