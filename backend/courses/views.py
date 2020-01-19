from rest_framework import permissions
from rest_framework.generics import UpdateAPIView
from .serializers import UserCorsesSerializer
from .models import Courses


class CreateUserCorse(UpdateAPIView):
    lookup_field = 'name'
    queryset = Courses.objects.all()
    serializer_class = UserCorsesSerializer
    permission_classes = permissions.IsAuthenticated







