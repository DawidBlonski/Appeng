from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = "accounts"
urlpatterns = [
    path("logout/", LogoutView.as_view(next_page = "appeng:home"),name="logout"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path("register/", views.register, name="register"),]

