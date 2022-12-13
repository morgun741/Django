from django.contrib import admin
from django.urls import path
from .views import (products_list_views, product_ditail_view, category_ditail_view)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_list_views, name='list'), # определили имена
    path('<int:pk>/', product_ditail_view, name='detail'), # это url-патерн для ссылки на индексный обьект в конкретном массиве словарей
    path('category/<int:pk>/', category_ditail_view, name='category')
]