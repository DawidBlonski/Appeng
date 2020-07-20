from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from courses.tests import create_sample_course
from courses.models import Words, Courses
from users.tests import create_sample_user
from .models import Answers
from users.models import Users

LOGIN_URL = reverse('users:login')
GET_WORD_URL = reverse('answers:get_word')


def create_sample_answer():
    user = Users.objects.get(pk=1)
    word = Words.objects.get(word='word')
    course = Courses.objects.get(name='test_name_course')
    Answers.objects.create(word=word, course=course, user=user)


class GetWordNoLoginTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_answers(self):
        print(self.__class__.__name__)
        response = self.client.put(GET_WORD_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class GetWordTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        user = create_sample_user()
        create_sample_course()
        create_sample_answer()
        payload = {'username': user.username, 'password': 'testpass'}
        response = self.client.post(LOGIN_URL, payload, format='json')
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))

    def test_answers(self):
        print(self.__class__.__name__)
        response = self.client.get(GET_WORD_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
