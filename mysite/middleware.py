from django.http import HttpResponseRedirect
from django.conf import settings
import os
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse
from appeng.models import Words

LOGIN_EXEMPT_URLS = [settings.LOGIN_URL.lstrip('/')]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    LOGIN_EXEMPT_URLS += [reverse(f'accounts:{expr}') for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        assert hasattr(request, 'user')
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(path in m for m in LOGIN_EXEMPT_URLS):
                return redirect_to_login(request.get_full_path())
        response = self.get_response(request)
        return response


class StartupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = r'appeng\data\words.txt'
        with open (path,'r') as file:
            file = [i.replace('\n','') for i in file.readlines()]

        [Words.objects.get_or_create(word = str(i)) for i in file]
        response = self.get_response(request)
        return response

