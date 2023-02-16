from django.shortcuts import render, redirect
#призвал форму с переопределением размеров полей
from .forms import AccountUserForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def upload_file(request):
    def handle_uploaded_file():
        with open("C:Users\Admin\PycharmProjects\Django\server\accounts\templates\accounts\name.txt", ) as f :
            f.read()
    if request.method == 'POST':
        form = AccountUserForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = AccountUserForm()
    return render(request, 'accounts/login.html', {'form':form} )




def account_login(request):
    #в reverse_lazy вставил нприложение а также  views-контроллер
    success_url = reverse_lazy('main:main')
    form = AccountUserForm()
    #для принятия данных только по пост запросу не используя GET

    if request.method == 'POST':
        form  = AccountUserForm(request.POST)
#на уровне метода is_valid() данные пришедшие через post-запрос
        if form.is_valid():
            #cleaned_data представляет из себя метод в который сбудут приходиить данные прошедшие валидацию, как тип данных
            # представуляет из себя словарь, данные из которого мы можем вытащить
            usr = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(
                username = usr,
                password = pwd
            )
        #провожу авторизацию пользователя
        #user передаём как экземпляр пользователя естественно аутентифицированный
            if user and user.is_active:
                login(request, user)
        # использую redirect для перенаправления пользователя на главную страницу
                return redirect(success_url)

    return render(request, 'accounts/login.html', {'form': form})
