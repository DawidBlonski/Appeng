from rest_framework import serializers
from appeng import models

class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ('id','word')

class User_answerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User_answer
        fields = ('id','words','current_user','answer')

class UserSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.User
        fields = ('id', 'username')

