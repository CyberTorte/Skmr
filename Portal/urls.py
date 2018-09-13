from django.urls import path

from . import views

app_name = 'Portal'
urlpatterns = [
    path('infomation/', views.infomation, name='infomation'),
]
