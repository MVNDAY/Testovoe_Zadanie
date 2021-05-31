from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'^register/$', views.register, name='register'),
]