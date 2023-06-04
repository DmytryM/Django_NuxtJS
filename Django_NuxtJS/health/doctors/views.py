from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': 'Про сайт', 'url_name': 'about'},
    {'title': 'Додати статтю', 'url_name': 'add_page'},
    {'title': 'Зворотній зв`язок', 'url_name': 'contact'},
    {'title': 'Увійти', 'url_name': 'login'},
]

def index(request):
    posts = Doctors.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'doctors/index.html', context=context)

def about(request):
    return render(request, 'doctors/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse('Add news')

def contact(request):
    return HttpResponse('Contact')

def login(request):
    return HttpResponse('Login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f"Відображення {post_id}")
