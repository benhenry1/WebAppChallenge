from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('user/<name>', views.user, name='user'),
	path('sn/<sn>', views.sn, name='sn'),
]