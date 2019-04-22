from rest_framework import viewsets, permissions
from appeng import models, serializers
from .permissions import IsOwner


class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]


class WordsViewset(viewsets.ModelViewSet):
    queryset = models.Words.objects.all()
    serializer_class = serializers.WordsSerializer


class User_answerViewset(viewsets.ModelViewSet):
    queryset = models.User_answer.objects.all()
    serializer_class = serializers.User_answerSerializer
    permission_classes = [IsOwner]
