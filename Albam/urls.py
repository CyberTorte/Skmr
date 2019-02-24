from django.urls import path

from . import views

app_name = 'Albam'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.AlbamDetailView.as_view(), name='detail'),
]
