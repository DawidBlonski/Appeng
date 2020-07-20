from rest_framework import serializers
from backend.courses.models import Words


class GetWord(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ('word',)
