from django.urls import path
from .views import GetWord, ChangeAnswer

app_name = 'answers'

urlpatterns = [
    path('get_word', GetWord.as_view(), name='get_word'),
    path(
        'change_answer/<int:word_id>',
        ChangeAnswer.as_view(),
        name='change_answer',
    ),
]
