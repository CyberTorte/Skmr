from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Albam/index.html'
    context_object_name = 'albam_list'

    def get_queryset(self):
        pass
