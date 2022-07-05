# Create your views here.
from django.shortcuts import render
from django.views import View

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'myblog/index.html'
        )