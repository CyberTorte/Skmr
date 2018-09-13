from django.urls import path

from . import views

app_name = 'selector'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('select/', views.selector, name='select'),
    path('produce', views.produce, name='produce'),
]
