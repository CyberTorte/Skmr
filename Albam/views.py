from django.shortcuts import render
from django.views import generic

from .models import Albam

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Albam/index.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(self, **kwargs)
        context['albam_list'] = Albam.objects.all().order_by('-updated_at')

        thumbnails = []
        for albam in Albam.objects.all().order_by('-updated_at').prefetch_related('photo_set'):
            thumbnails.append(albam.photo_set.all().order_by('id').first())

        context['thumbnails'] = thumbnails

        return context
