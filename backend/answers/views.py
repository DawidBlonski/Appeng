from django.core.cache import cache
from .models import Answers
from courses.models import Courses
from .serializers import GetWord
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


# Create your views here.
class GetWord(GenericAPIView):
    serializer_class = GetWord
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get_active_course():
        course_id = cache.get('course')
        return course_id

    def get(self, request, *args, **kwargs):
        course_id = self.get_active_course()
        user = self.request.user
        if not course_id:
            return Response('You are not have active course')
        if Courses.user_in_course(user=user, course=course_id):
            random_word = Answers.objects.random(user=user, course=course_id)
            if random_word:
                serializer = self.get_serializer(random_word)
                return Response(serializer.data)
            else:
                return Response('YOU FINISHED COURSE')

        else:
            return Response('You are not subscribed this course')


class ChangeAnswer(APIView):
    def get(self, request, word_id):
        user = self.request.user
        if user.is_authenticated:
            answer_query = Answers.objects.filter(user=user, word_id=word_id)
            answer_value = answer_query.values_list('answer', flat=True)
            if answer_value[0]:
                return Response(answer_value)
            else:
                answer_value = answer_query.update(answer=True)
                return Response(answer_value)
