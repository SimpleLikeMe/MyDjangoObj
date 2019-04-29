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
    url('^borrowing/(\d+)/$', views.borrowing, name='borrowing'),
    url('^history/$', views.history, name='history'),
    url('^modify/$', views.modify, name='modify'),
    url('^active/(\d+)/$', views.active_account, name='active'),
]
