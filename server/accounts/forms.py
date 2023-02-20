from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
class AccountUserForm(forms.Form):
    #в логин html мы рапссматриваем поле с username
    #однако атрибут label может иметь совсем другое значение

    '''атрибут widget работает также для поля username,
    однако название класса необходимо менять в зависимости
    от типа контента обрабатываемого поля, а также изменять значение словаря в зависимости
     от названия поля'''

    username = forms.CharField(label = 'Login', max_length = 150,
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'field_username'}
                               )
                               )
    '''сделаем сокрытым поле, ввода пароля
    это реализуется через атрибут attrs, который принимает
    значение словаря, и в зависимости от подборки ключа и значения
    воздействует на поле с паролем'''
    password = forms.CharField(max_length = 250,
                               widget=forms.widgets.PasswordInput(
                                   attrs={'class': 'field_password'}
                               ))
    file = forms.FileField()
    birth_day = forms.DateField(widget=forms.widgets.DateInput())

# class AccountUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'birth_day', 'file')
#         widgets = {
#             'username': forms.widgets.TextInput(attrs={'class': 'field_username'}),
#             'password': forms.widgets.PasswordInput(attrs={'class': 'field_password'}),
#             'birth_day': forms.widgets.DateInput(attrs={'class': 'form-control'}),
#             'file': forms.widgets.FileInput()
#         }