from django.core.cache import cache
from .models import Answers
from courses.models import Courses,Words
from .serializers import GetWord,Word
from rest_framework.generics import GenericAPIView
from random import randint
from rest_framework.response import Response


# Create your views here.
class GetWord(GenericAPIView):
    serializer_class = Word


    def get(self, request, *args, **kwargs):
        name = cache.get('course')
        user = self.request.user
        try:
            course = Courses.objects.get(name=name).id
        except Courses.DoesNotExist:
            course = None
        if course and user:
            answers = Answers.objects.filter(user=user, answer=False, course=course)
            answers_word = answers.values('word')
            answers_count = answers_word.count() - 1
            rand = randint(0, answers_count)
            word = answers_word[rand]
            word = Words.objects.filter(id=word['word']).values_list('id',flat=True)
            serializer = self.get_serializer(word)
            return Response(serializer.data)

        else:
            return Response('')


