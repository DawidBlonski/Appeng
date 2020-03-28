from django.db import models
from courses.models import Words,Courses
from django.contrib.auth import get_user_model
user = get_user_model()

class Answers(models.Model):
    user = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    word = models.ForeignKey(Words,on_delete=models.DO_NOTHING)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.course} {self.word} {self.answer}"

