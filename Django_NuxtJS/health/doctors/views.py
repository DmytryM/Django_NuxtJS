from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import *
from .models import *

menu = [
    {'title': 'Про сайт', 'url_name': 'about'},
    {'title': 'Додати статтю', 'url_name': 'add_page'},
    {'title': 'Зворотній зв`язок', 'url_name': 'contact'},
    {'title': 'Увійти', 'url_name': 'login'},
]


class DoctorsHome(ListView):
    model = Doctors
    template_name = 'doctors/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Головна сторінка'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Doctors.objects.filter(is_published=True)


# def index(request):
#     posts = Doctors.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'doctors/index.html', context=context)


def about(request):
    return render(request, 'doctors/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'doctors/addpage.html', {'form':form, 'menu': menu, 'title': 'Додати'})


def contact(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_post(request, post_slug):
#     post = get_object_or_404(Doctors, slug=post_slug)
#
#     context = {
#
#         'post': post,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'doctors/post.html', context=context)

class ShowPost(DetailView):
    model = Doctors
    template_name = 'doctors/post.html'

class DoctorsCategory(ListView):
    model = Doctors
    template_name = 'doctors/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Doctors.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категорія - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context


# def show_category(request, cat_id):
#     posts = Doctors.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'doctors/index.html', context=context)
