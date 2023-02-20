from django.shortcuts import render, redirect
#призвал форму с переопределением размеров полей
from .forms import AccountUserForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import User


def upload_file(request):
    # def handle_uploaded_file():
    #     with open("C:Users\Admin\PycharmProjects\Django\server\accounts\templates\accounts\name.txt", ) as f :
    #         f.read()
    if request.method == 'POST':
        form = AccountUserForm(request.POST, request.FILES)
        if form.is_valid():
            # takes_f = User(
            #     form.cleaned_data['username'],
            #     form.cleaned_data['password'],
            #     form.cleaned_data['file'],
            #     form.cleaned_data['birth_day']
            # )
            # takes_f.save()
            # data = User(
            #     file=request.FILES.get('file'),
            #     username=request.FILES.get('username'),
            #     password=request.FILES.get('password'),
            #     birth_day=request.POST.get('birth_day')
            # )
            # data.save()
            #instance = User(file=request.FILES['file'])
            file = form.cleaned_data.get('file')
            if file :
                print('Да файловый обьект был извлечён')
            else:
                print('file')
            # instance.save()
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
        form  = AccountUserForm(request.POST, request.FILES)
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
                User.objects.get(username=usr)
                login(request, user)
        # использую redirect для перенаправления пользователя на главную страницу
                return redirect(success_url)

    return render(request, 'accounts/login.html', {'form': form})
