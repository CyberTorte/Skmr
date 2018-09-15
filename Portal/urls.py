from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'Portal'
urlpatterns = [
    path('', RedirectView.as_view(url='infomation/')),
    path('infomation/', views.infomation, name='infomation'),
]
