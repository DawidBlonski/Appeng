
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appeng.urls', namespace='appeng')),
    path('', include('accounts.urls', namespace='accounts')),
]
