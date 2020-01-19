from django.urls import path
from .views import CreateUserCorse

app_name = 'courses'

urlpatterns = [
    path('user_course/<slug:name>', CreateUserCorse.as_view(), name='user_course'),
]
