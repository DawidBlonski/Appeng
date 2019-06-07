from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from appeng.models import Words, User_answer
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class Test_vievs_status(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {}
        self.login_required_url = ["logout"]
        self.login_anonymus_url = ["login", "register"]

    def test_login_user(self):
        for url in self.login_required_url:
            response = self.client.post(
                reverse(f"accounts:{url}"), self.credentials, follow=False
            )
            self.failUnlessEqual(response.status_code, 302)

    def test_anonymus_user(self):
        for url in self.login_anonymus_url:
            response = self.client.post(
                reverse(f"accounts:{url}"), self.credentials, follow=False
            )
            self.failUnlessEqual(response.status_code, 200)


class ModelTest(TestCase):
    def create_user(self):
        return User.objects.create_user("test", "test@test.com", "test")

    def create_words(self):
        return Words.objects.create(word="test")

    def create_user_answer(self):
        user = self.create_user()
        return User_answer.objects.get_or_create(current_user=user)

    def test_words_creation(self):
        word = self.create_words()
        self.assertTrue(isinstance(word, Words))
        self.assertEqual(word.__str__(), word.word)

    def test_user(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), user.username)


class TestAccounts(StaticLiveServerTestCase):
    def setUp(self):
        self.user = User.objects.create_user("test", "test@test.com", "TeSt412")

        self.user.is_active = True
        self.user.save()
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)
        self.login_url = "%s%s" % (self.live_server_url, reverse_lazy("accounts:login"))
        self.register_url = "%s%s" % (
            self.live_server_url,
            reverse_lazy("accounts:register"),
        )

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("login").click()
        self.assertIn(self.login_url, self.browser.current_url)

    def test_register(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("register").click()
        self.assertIn(self.register_url, self.browser.current_url)

    def test_login_user(self):
        self.browser.get(
            "%s%s" % (self.live_server_url, reverse_lazy("accounts:login"))
        )
        self.browser.find_element_by_id("id_username").send_keys("test")
        self.browser.find_element_by_id("id_password").send_keys("TeSt412")
        self.browser.find_element_by_id("submit").click()
        self.assertIn(self.live_server_url, self.browser.current_url)
