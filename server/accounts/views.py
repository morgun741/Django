from django.shortcuts import render

def account_login(request):
    return render(request, 'accounts/login.html')
