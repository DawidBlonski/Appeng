from rest_framework import serializers
from courses.models import Words


class GetWord(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ('word',)
