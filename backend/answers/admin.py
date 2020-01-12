from django.contrib import admin
from .models import Answers

@admin.register(Answers)
class AuthorAdmin(admin.ModelAdmin):
    pass