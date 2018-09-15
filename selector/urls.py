from django.urls import path

from . import views

app_name = 'selector'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('result/', views.selector, name='result'),
    path('produce/', views.produce, name='produce'),
]
