from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import User_answer

@receiver(m2m_changed, sender=User_answer.words.through)
def users_answer_changed(sender, instance, **kwargs):
    instance.user_score = instance.words.count()
    instance.save()