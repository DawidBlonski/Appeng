from appeng import views
from django.urls import path


app_name = "appeng"

urlpatterns = [
    path("", views.home, name="home"),
    path("connect/", views.set_course, name="set_course"),
    path("connect/<str:operation>/<int:pk>", views.change_answer, name="change_answer"),
]
