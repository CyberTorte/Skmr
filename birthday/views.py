from django.shortcuts import render
from django.views import generic

from .models import Photo

# Create your views here.

class NatsumiBirthdayView(generic.ListView):
    template_name = 'birthday/2018/Natsumi.html'
    context_object_name = 'photo_list'

    def get_queryset(self):
        # データを再編成しテンプレートに返す
        photo_list = Photo.objects.filter(person='Natsumi', year=2018).order_by('serial')
        photo_list = sort_photo(photo_list)
        return photo_list

class KaoruBirthdayView(generic.ListView):
    template_name = 'birthday/2018/Kaoru.html'
    context_object_name = 'photo_list'

    def get_queryset(self):
        # データを再編成しテンプレートに返す
        photo_list = Photo.objects.filter(person='Kaoru', year=2018).order_by('serial')
        photo_list = sort_photo(photo_list)
        return photo_list


def sort_photo(photo_list):
    top_photo_list = []
    message_photo_list = []
    sponsor_photo_list = []
    final_photo_list = []
    sorted_photo_list = []

    # 分類ごとに分ける
    for photo in photo_list:
    
        if photo.kind == 'top':
            top_photo_list.append(photo)
        
        elif photo.kind == 'message':
            message_photo_list.append(photo)

        elif photo.kind == 'sponsor':
            sponsor_photo_list.append(photo)

        elif photo.kind == 'final':
            final_photo_list.append(photo)

    # 分けたものを一本化する
    sorted_photo_list.extend(top_photo_list)
    sorted_photo_list.extend(message_photo_list)
    sorted_photo_list.extend(sponsor_photo_list)
    sorted_photo_list.extend(final_photo_list)

    return sorted_photo_list