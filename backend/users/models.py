from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    bio = models.TextField()

    def __str__(self):
        return self.username
