from django.shortcuts import render
#призвал форму с переопределением размеров полей
from .forms import AccountUserForm
def account_login(request):
    form = AccountUserForm()
    #для принятия данных только по пост запросу не используя GET

    if request.method == 'POST':
        print(request.POST)
    return render(request, 'accounts/login.html', {'form': form})
