from django.http import HttpResponseNotFound
from django.shortcuts import render

# from .forms import AddCommentForm
# from .forms import AddRecords
from .models import *
from django.views.generic import ListView, DetailView, CreateView

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Услуги и цены', 'url_name': 'services'},
        # {'title': 'Запись', 'url_name': 'records'},
        {'title': 'Отзывы', 'url_name': 'comment'},
        # {'title': 'Портфолио', 'url_name': 'public'},
        # {'title': 'Наши мастера', 'url_name': 'worker'},

        ]


class HomePage(ListView):
    # класс отображения главной страницы с публикациями и новостной лентой
    model = Publications
    template_name = 'blog/home.html'
    context_object_name = 'public'

    # метод передает статические и динамические данные
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'

        # context['cat_selected'] = 0 #поле для выбранной категории в шаблоне
        return context

# метод опредедяет читать только опубликованные записи из таблицы
    def get_queryset(self):
        return Publications.objects.filter(is_published=True)


class ShowPublic(DetailView):
    #класс формирования динамической ссылки на кнопку <подробнее>
    model = Publications
    template_name = 'blog/public.html'
    slug_url_kwarg = 'public_slug'
    context_object_name = 'public'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['public']
        context['menu'] = menu
        return context


class Comment(ListView):
    model = Comment
    template_name = 'blog/comment.html'
    context_object_name = 'comm'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Отзывы'
        return context


# class Records(CreateView):
#     form_class = AddRecords
#     template_name = 'blog/records.html'
#     context_object_name = 'rec'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Запись'
#         return context

# class AddComment(CreateView):
#     form_class = AddCommentForm
#     template_name = 'blog/add_comment.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Добавить отзыв'
#         return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
