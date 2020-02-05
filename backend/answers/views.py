from django.shortcuts import render
from .models import Answers
from courses.models import Courses
from .serializers import GetWord

from rest_framework.generics import ListAPIView
# Create your views here.
class GetWord(ListAPIView):
    serializer_class = GetWord
    queryset = Answers.objects.all()


    def get_queryset(self):
        user = self.request.user.id
        cours  = Courses.objects.get(name='123').id
        queryset = Answers.objects.filter(user = user,answer=False,cours=cours)
        return queryset




