from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Courses
from users.models import Users



class UserCorsesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        exclude =  ('word','name','user')

    def update(self, instance, validated_data):
        user = self.context['request'].user.id
        user = Users.objects.filter(id=user)
        validated_data['user'] = user
        return super().update(instance, validated_data)


