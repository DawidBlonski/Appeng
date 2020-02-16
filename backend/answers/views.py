from django.core.cache import cache
from .models import Answers
from courses.models import Courses,Words
from .serializers import GetWord,Word
from rest_framework.generics import ListAPIView
from random import randint

# Create your views here.
class GetWord(ListAPIView):
    serializer_class = Word

    def get_queryset(self):
        name = cache.get('course')
        user = self.request.user
        try:
            cours = Courses.objects.get(name=name).id
        except Courses.DoesNotExist:
            cours = None

        if cours and user:
            answers = Answers.objects.filter(user=user, answer=False, cours=cours)
            answers_word = answers.values('word')
            answers_count = answers_word.count() - 1
            rand = randint(0, answers_count)
            word = answers_word[rand]
            return Words.objects.filter(id=word['word'])

        else:
            return Words.objects.none()



