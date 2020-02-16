from django.http import HttpResponse
from django.core.cache import cache
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView,ListAPIView
from rest_framework.views import APIView
from .serializers import UserCorsesSerializer,CourseList
from .models import Courses

class CourseList(ListAPIView):
    serializer_class = CourseList
    queryset = Courses.objects.all()
    #permission_classes = (permissions.IsAuthenticated,)


class UpdateUserCourse(UpdateAPIView):
    lookup_field = 'name'
    queryset = Courses.objects.all()
    serializer_class = UserCorsesSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SetCourse(APIView):
    serializer_class = CourseList

    def get(self,requests,name):
        cache.set('course',name)
        return HttpResponse('')







