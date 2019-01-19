from django.contrib import admin

from .models import Photo

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_filter = [
        'kind',
        'person',
        'year'
    ]

admin.site.register(Photo, PhotoAdmin)
