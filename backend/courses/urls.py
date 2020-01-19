from django.urls import path
from .views import UpdateUserCorse,CourseList

app_name = 'courses'

urlpatterns = [
    path('user_course/<slug:name>', UpdateUserCorse.as_view(), name='user_course'),
    path('course_list/',CourseList.as_view(),name='course_list')
]
