from django.contrib import admin

from .models import (
    Albam,
    Photo
)

# Register your models here.

class AlbamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'updated_at'
    )

admin.site.register(Albam, AlbamAdmin)

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