from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import *

menu = [
    {'title': 'Про сайт', 'url_name': 'about'},
    {'title': 'Додати', 'url_name': 'add_page'},
    {'title': 'Зворотній зв`язок', 'url_name': 'contact'},
    {'title': 'Увійти', 'url_name': 'login'},
]


class DoctorsHome(DataMixin, ListView):
    model = Doctors
    template_name = 'doctors/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(c_def.items()))

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
    return render(request, 'doctors/about.html', {'menu': menu, 'title': 'Про сайт'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'doctors/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Додати")
        return dict(list(context.items()) + list(c_def.items()))


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'doctors/addpage.html', {'form':form, 'menu': menu, 'title': 'Додати'})


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

class ShowPost(DataMixin, DetailView):
    model = Doctors
    template_name = 'doctors/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class DoctorsCategory(DataMixin, ListView):
    model = Doctors
    template_name = 'doctors/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Doctors.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категорія - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

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
