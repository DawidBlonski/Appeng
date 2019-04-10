from django.urls import path
from accounts import views
from django.conf.urls import url
from django.contrib.auth.views import (
    login,logout,)
app_name = 'accounts'

urlpatterns = [
    path('logout/',logout, {'template_name': 'logged_out.html'}, name='logout'),
	path('login/', login, {'template_name': 'login.html'}, name='login'),
	path('register/', views.register, name = 'register')
]