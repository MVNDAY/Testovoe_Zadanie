from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^getcounter/(?P<counter_id>\d+)/$', views.getcounter, name='getcounter'),
	url(r'^changecounter/(?P<counter_id>\d+)/$', views.changecounter, name ='changecounter'),
]