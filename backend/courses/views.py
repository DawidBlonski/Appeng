from django.core.cache import cache
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserCorsesSerializer, CourseList
from .models import Courses
from answers.models import Answers


class CourseList(ListAPIView):
    serializer_class = CourseList
    queryset = Courses.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class SetUserCourse(UpdateAPIView):
    lookup_field = 'name'
    serializer_class = UserCorsesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return Courses.objects.get(name=self.kwargs['name'])

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        curren_user_id = request.user.id
        user_is_in_course = instance.__class__.objects.values_list(
            'user'
        ).filter(user=curren_user_id)
        if not user_is_in_course:
            Answers.create_answers(instance, request.user)
            instance.user.add(curren_user_id)
            return Response('')
        else:
            Answers.delete_answers(instance, request.user)
            instance.user.remove(curren_user_id)
            return Response('')


class CacheCourse(APIView):

    serializer_class = CourseList

    @staticmethod
    def get(requests, name):
        course = Courses.objects.get(name=name).id
        cache.set('course', course)
        return Response('')
