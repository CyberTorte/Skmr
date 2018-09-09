from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'birthday'
urlpatterns = [
    path('Natsumi/', views.NatsumiBirthdayView.as_view(), name='Natsumi'),
    path('skmr/Natsumi/', RedirectView.as_view(url='/birthday/Natsumi/')),
    path('skmr/Kaoru/', views.KaoruBirthdayView.as_view(), name='Kaoru'),
    path('Kaoru/', RedirectView.as_view(url='/birthday/skmr/Kaoru/')),
]
