from django.contrib import admin
from .models import Words, Courses


@admin.register(Words)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Courses)
class AuthorAdmin(admin.ModelAdmin):
    pass
