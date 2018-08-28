from django.shortcuts import render
from django.views import generic

from .models import Photo

# Create your views here.

class NatsumiIndexView(generic.ListView):
    template_name = ''
    context_object_name = 'photo_list'

    def get_queryset(self):
        # データを再編成しテンプレートに返す
        photo_list = Photo.objects.all().order_by('id')

def sort_photo(photo_list):
    for 