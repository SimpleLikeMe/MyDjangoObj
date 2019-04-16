from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^list/$', views.book_list),
    url(r'^detail/([0-9]+)/$', views.detail),
]
