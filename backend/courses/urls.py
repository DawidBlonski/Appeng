from django.urls import path
from .views import SetUserCourse,CourseList,CacheCourse

app_name = 'courses'

urlpatterns = [
    path('set_user_course/<slug:name>', SetUserCourse.as_view(), name='user_course'),
    path('course_list/',CourseList.as_view(),name='course_list'),
    path('setcourse/<slug:name>',CacheCourse.as_view(), name = 'set_course')
]
