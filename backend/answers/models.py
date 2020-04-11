from django.db import models
from courses.models import Words
from django.contrib.auth import get_user_model
from courses.models import Courses
user = get_user_model()

class Answers(models.Model):
    user = models.ForeignKey(user,on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    word = models.ForeignKey(Words,on_delete=models.DO_NOTHING)
    answer = models.BooleanField(default=False)

    @classmethod
    def create_answers(cls,course,user):
        word_in_course = course.__class__.objects.values_list('word',flat=True)
        for word in word_in_course:
            word = Words.objects.get(id=word)
            Answers.objects.create(word=word, course=course, user=user)

    @classmethod
    def delete_answers(cls,course,user):
        Answers.objects.filter(course=course, user=user).delete()


    def __str__(self):
        return f"{self.user} {self.course} {self.word} {self.answer}"

