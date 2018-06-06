
from django.conf.urls import include, url
from hawkeye.views import *
from . import views
app_name = 'hawkeye'

urlpatterns = [
    url('', views.index, name='index'),
    #url(r'^result/$', views.result, name='result')
]