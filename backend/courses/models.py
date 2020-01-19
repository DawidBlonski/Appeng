from django.db import models
from users.models import Users

class Words(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word

class Courses(models.Model):
    name = models.CharField(max_length=50,unique=True)
    user = models.ManyToManyField(Users,blank=True,related_name='user_cur')
    word = models.ManyToManyField(Words, blank=True)


    def __str__(self):
        return self.name


