from django.urls import path
#from .views import account_login
from .views import upload_file

app_name = 'accounts'

#urlpatterns = [ path('', account_login, name='login') ]
urlpatterns = [ path('', upload_file, name='file') ]