from django.contrib import admin
from django.urls import path
from .views import (contacts, description, index)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('description/', description),
    path('index/', index)
]