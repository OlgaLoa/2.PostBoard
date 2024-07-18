from django.db import models
from django.contrib.auth.models import AbstractUser
from django_summernote.widgets import SummernoteWidget



# МОДЕЛЬ АВТОРА-ПОЛЬЗОВАТЕЛЯ
class AuthorUser(AbstractUser):
    name_of_user = models.CharField(max_length = 64, unique=True)
    def __str__(self):
        return self.username

# МОДЕЛЬ КАТЕГОРИИ
class Category(models.Model): #
    CATEGORY_CHOICES = (
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('DD', 'ДД'),
        ('Traders', 'Торговцы'),
        ('Guildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Leatherworkers', 'Кожевники'),
        ('Potions_Masters', 'Зельевары'),
        ('Spell_Masters', 'Мастеразаклинаний'))
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='Tanks')  # поле с выбором категории;

    def __str__(self):
        return self.category

# МОДЕЛЬ ПОСТА
# Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент.
# пользователь обязательно должен определить объявление в одну из категорий
class Post(models.Model):# содержать в себе статьи и новости, которые создают пользователи
    title_of_the_post = models.CharField(max_length=128)  # заголовок поста;
    text_of_the_post = SummernoteWidget() # текст поста с изображ;
    category_of_the_post = models.ForeignKey(Category, on_delete = models.CASCADE)# у одной категории мб много постов;
    author_of_the_post = models.ForeignKey(AuthorUser, on_delete=models.CASCADE)  # у одного автора мб много постов;


    def __str__(self):
        return f'{self.author_of_the_post } : {self.category_of_the_post} : {self.title_of_the_post} : {self.text_of_the_post}'


# МОДЕЛЬ ОТКЛИКА
# Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста.
class Response(models.Model):
    text_of_the_response = models.CharField(max_length=128)  # заголовок поста;
    post_of_the_response = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_of_the_response = models.ForeignKey(AuthorUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_of_the_response