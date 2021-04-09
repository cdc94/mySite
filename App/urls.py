from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path, path
import controller

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'admin/', admin.site.urls),
    url(r'index/', controller.flowStatController),
]