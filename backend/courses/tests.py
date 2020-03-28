from django.test import TestCase
from django.urls import reverse
from courses.models import Courses
from rest_framework.test import APIClient
from rest_framework import status
from courses.models import Words
from django.core.cache import cache


GET_COURSES_LIST  = reverse('courses:course_list')
USER_COURSE = reverse('courses:user_course',kwargs={'name':'test_name_course'})
SET_COURSE = reverse('courses:set_course', kwargs={'name': 'test_name_course'})
LOGIN_URL = reverse('users:login')




def create_sample_words():
    return Words.objects.create(word ='word')

def create_sample_course():
    create_sample_words()
    word = Words.objects.get(word= 'word')
    course = Courses.objects.create(name = 'test_name_course')
    cache.set('course','test_name_course')
    course.word.add(word)
    return Courses.objects.get(name='test_name_course')


class CoursesNoLoginTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_courses_list(self):
        print(self.__class__.__name__)
        response = self.client.put(GET_COURSES_LIST)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_user_course(self):
        print(self.__class__.__name__)
        response = self.client.put(SET_COURSE)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_setcourse(self):
        print(self.__class__.__name__)
        response = self.client.put(USER_COURSE)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class CoursesLoginTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        payload = {'username': user.username, 'password': 'testpass'}
        response = self.client.post(LOGIN_URL, payload, format='json')
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))

    def test_courses_list(self):
        print(self.__class__.__name__)
        response = self.client.get(GET_COURSES_LIST)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




