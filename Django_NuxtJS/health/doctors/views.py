from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

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
        'title': 'Главная страница',
        'cat_selected': 0,
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


def show_post(request, post_slug):
    post = get_object_or_404(Doctors, slug=post_slug)

    context = {

        'post': post,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': post.cat_id,
    }

    return render(request, 'doctors/post.html', context=context)


def show_category(request, cat_id):
    posts = Doctors.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'doctors/index.html', context=context)
