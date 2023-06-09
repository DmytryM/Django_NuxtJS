from django.db.models import Count
from .models import *

menu = [{'title': "Про сайт", 'url_name': 'about'},
        {'title': "Додати", 'url_name': 'add_page'},
        {'title': "Зворотій зв'язок", 'url_name': 'contact'},
        {'title': "Лікарні", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('doctors'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
