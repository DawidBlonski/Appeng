from django.urls import path
from accounts import views
from django.contrib.auth.views import login, logout

app_name = "accounts"
urlpatterns = [
    path("logout/", logout,{'next_page': 'appeng:home'},name="logout"),
    path("login/", login, {"template_name": "login.html"}, name="login"),
    path("register/", views.register, name="register"),
]
