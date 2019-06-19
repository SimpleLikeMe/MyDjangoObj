from django.conf.urls import url
from . import views

app_name = 'shopping'

urlpatterns = [
    url('^$', views.index, name='index'),
]



