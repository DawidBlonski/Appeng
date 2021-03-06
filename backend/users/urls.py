from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from users.views import RegisterUserView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', obtain_jwt_token, name='login'),
]
