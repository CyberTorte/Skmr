from django.contrib import admin

from .models import song

# Register your models here.

class Song_Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'attribute', 'difficulty', 'level', 'artist', 'style', 'limited', 'party')
    list_filter = ['attribute', 'difficulty', 'limited']

admin.site.register(song, Song_Admin)
