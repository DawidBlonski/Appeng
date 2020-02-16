from django.urls import path
from .views import UpdateUserCourse,CourseList,SetCourse

app_name = 'courses'

urlpatterns = [
    path('user_course/<slug:name>', UpdateUserCourse.as_view(), name='user_course'),
    path('course_list/',CourseList.as_view(),name='course_list'),
    path('setcourse/<slug:name>',SetCourse.as_view(), name = 'set_course')
]
