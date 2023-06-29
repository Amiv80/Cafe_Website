from django.contrib import admin
from django.urls import path, include
from cafe.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cafe.urls')),
]
