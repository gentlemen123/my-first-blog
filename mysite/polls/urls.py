from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^time/$', views.current_time, name='time'),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead, name='hours_ahead'),
]