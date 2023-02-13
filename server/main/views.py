from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
#клепаю шаблоны с контекстом и заставляю сервер их обрабатывать
def main(request):
    #template = Template('Hello {{name}}')
    #context = Context({'name': 'Oleg'})
    template = get_template('main\index.html')       #выше низкого

    """в данном случае не потребуется использовать
    обьект Context модуля django.template, т.к. 
    get_template сделает его самостоятельно"""

    context = {'name': 'Oleg'}                       #выше низкого
    return HttpResponse(template.render(context))    #выше низкого
    #return render(request, 'main\index.html')       #низкий уровень обработки запроса и отсылки пользователя на сервак
def description(request):
    return render(request, 'main\description.html', {'description': 'Информация о проекте, который сделал я'})

def contacts(request):
    render_page = render_to_string('main\contacts.html',
    {'contacts': ['Контакт 1', 'Контакт 2', 'Контакт 3']}
    )                                                #средний уровень
    return HttpResponse(render_page)                 #средний уровень
    #return render(request, 'main\contacts.html')


