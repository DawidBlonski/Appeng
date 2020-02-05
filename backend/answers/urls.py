from django.urls import path
from .views import GetWord

app_name = 'answers'

urlpatterns = [
    path('', GetWord.as_view(), name='word'),

]
