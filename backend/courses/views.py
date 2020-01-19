from rest_framework import permissions
from rest_framework.generics import UpdateAPIView,ListAPIView
from .serializers import UserCorsesSerializer,CourseList
from .models import Courses

class CourseList(ListAPIView):
    serializer_class = CourseList
    queryset = Courses.objects.all()
    #permission_classes = (permissions.IsAuthenticated,)


class UpdateUserCorse(UpdateAPIView):
    lookup_field = 'name'
    queryset = Courses.objects.all()
    serializer_class = UserCorsesSerializer
    permission_classes = (permissions.IsAuthenticated,)







