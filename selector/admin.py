from django.contrib import admin

from .models import Song

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'attribute', 'difficulty', 'level', 'artist', 'style', 'limited', 'party')
    list_filter = ['attribute', 'difficulty', 'artist', 'limited']

admin.site.register(Song, SongAdmin)
