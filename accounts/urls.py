from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = "accounts"
urlpatterns = [
    path("logout/", LogoutView,{'next_page': 'appeng:home'},name="logout"),
    path("login/", LoginView, {"template_name": "login.html"}, name="login"),
    path("register/", views.register, name="register"),
]
