from django.db import models
from backend.users.models import Users


class Words(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word


class Courses(models.Model):

    name = models.CharField(max_length=50, unique=True)
    user = models.ManyToManyField(Users, related_name='user_cur', blank=True)
    word = models.ManyToManyField(Words, blank=True)

    @staticmethod
    def user_in_course(user, course):
        users_in_course = Courses.objects.filter(user=user.id, pk=course)
        if users_in_course:
            return True
        else:
            return False

    def __str__(self):
        return self.name
