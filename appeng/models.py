from django.db import models
from django.contrib.auth.models import User


class Words(models.Model):
    word = models.CharField(max_length=40)

    def __str__(self):
        return self.word


class User_anwer_QuerySet(models.QuerySet):
    @classmethod
    def get_user_answer(cls, current_user):
        user_answers = User_answer.objects.get(current_user=current_user).words.all()
        return user_answers

    @classmethod
    def get_user_not_answer(cls, current_user):
        user_answers = cls.get_user_answer(current_user=current_user)
        words = Words.objects.exclude(id__in=user_answers).order_by("?").first()
        return words


    @classmethod
    def course_final_score(cls, current_user):
        win_score = Words.objects.all().count()
        return win_score


class User_answer(models.Model):
    words = models.ManyToManyField(Words, blank=True,related_name = 'user_words')
    current_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    answer = models.BooleanField(default=True)
    user_score = models.PositiveIntegerField(db_index=True, default=0)
    def __str__(self):
        return str(self.current_user)

    @classmethod
    def know_word(cls, current_user, user_answer):
        answer, created = cls.objects.get_or_create(current_user=current_user)
        answer.words.add(user_answer)

    @classmethod
    def dont_know_word(cls, current_user, user_answer):
        answer, created = cls.objects.get_or_create(current_user=current_user)
        answer.words.remove(user_answer)
