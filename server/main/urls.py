from django.contrib import admin
from django.urls import path
from .views import (contacts, description, main)

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('description/', description),
    path('main', main, name = "main")
]