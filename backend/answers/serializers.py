from rest_framework import serializers
from .models import Answers
from courses.models import Words


class Word(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ('word',)

class GetWord(serializers.ModelSerializer):
    word = Word(read_only=True)
    class Meta:
        model = Answers
        fields = ('word',)

