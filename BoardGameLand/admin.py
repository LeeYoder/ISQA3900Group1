from django.contrib import admin

from .models import Genre, Game

admin.site.register(Game)
admin.site.register(Genre)
