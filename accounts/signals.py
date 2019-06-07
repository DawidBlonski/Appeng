from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_logged_in)
def login_signal(sender, user, request, **kwargs):
    messages.success(request, "Success login")


@receiver(user_logged_out)
def logout_signal(sender, user, request, **kwargs):
    messages.success(request, "Success logout")
