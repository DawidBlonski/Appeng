
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appeng.urls', namespace='appeng')),
    path('', include('accounts.urls', namespace='accounts')),
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken'))
]
