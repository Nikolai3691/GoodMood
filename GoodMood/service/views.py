from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView

from blog.views import menu
from .models import *


class Services(ListView):
    """класс отображения списка услуг и цен"""
    model = Services
    template_name = 'service/services.html'
    context_object_name = 'servic'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Услуги и цены'
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')