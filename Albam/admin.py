from django.contrib import admin

from .models import (
    Albam,
    Card,
    Picture,
    Photo
)

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'albam_id',
        'title',
        'creater',
        'created_at'
    )
    list_filter = [
        'albam_id',
        'creater'
    ]

admin.site.register(Photo, PhotoAdmin)

admin.site.register(Picture)

class PictureInline(admin.TabularInline):
    model = Picture
    extra = 0

class CardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'albam',
        'title',
        'creater',
        'created_at'
    )
    list_filter = [
        'albam',
        'creater'
    ]
    inlines = [PictureInline]

admin.site.register(Card, CardAdmin)

class CardInline(admin.TabularInline):
    model = Card
    extra = 0

class AlbamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'updated_at'
    )
    inlines = [CardInline]

admin.site.register(Albam, AlbamAdmin)
