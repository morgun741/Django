from django import forms

class AccountUserForm(forms.Form):
    #в логин html мы рапссматриваем поле с username
    #однако атрибут label может иметь совсем другое значение

    атрибут widget работает также для поля username,
    однако название класса необходимо менять в зависимости
    от типа контента обра

    username = forms.CharField(label = 'Login', max_length = 150)
    '''сделаем сокрытым поле, ввода пароля
    это реализуется через атрибут attrs, который принимает
    значение словаря, и в зависимости от подборки ключа и значения 
    воздействует на поле с паролем'''
    password = forms.CharField(max_length = 250,
                               widget=forms.widgets.PasswordInput(
                                   attrs={'class': 'field_password'}
                               ))