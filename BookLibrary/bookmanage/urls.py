from django.conf.urls import url
from . import views

app_name = 'bookmanage'

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^login/$', views.login, name='login'),
    url('^register/$', views.register, name='register'),
    url('^home/$', views.home, name='home'),
    url('^query/$', views.query, name='query'),
    url('^bookinfo/(\d+)/$', views.book_info, name='bookinfo'),
    url('^info/$', views.info, name='info'),
    url('^history/$', views.history, name='history'),
    url('^modify/$', views.modify, name='modify'),
]
