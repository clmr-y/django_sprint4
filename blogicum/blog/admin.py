"""Unused."""

from django.contrib import admin
from .models import Post, Category, Location, Comment

"""Название приложения Blog переведите на русский: «Блог»
Переведите названия моделей:
Название модели	Единственное число	Множественное число
Category	категория	Категории
Location	местоположение	Местоположения
Post	публикация	Публикации"""


admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
