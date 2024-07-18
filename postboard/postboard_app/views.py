
from .models import Post
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView
from .forms import PostForm
from django.shortcuts import render



class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'id'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'post_list.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'post_list'


# PermissionRequiredMixin,
class PostCreate(CreateView):
    permission_required = ('postboard_app.add_post') #add_post из админки Chosen permissions
    form_class = PostForm # Указываем нашу разработанную форму
    model = Post # модель
    template_name = 'post_create.html' #новый шаблон, в котором используется форма.

