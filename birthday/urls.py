from django.urls import path

from . import views

app_name = 'birthday'
urlpatterns = [
    path('', views.NatsumiBirthdayView.as_view(), name='Natsumi'),
]
