"""Skmr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from selector import views as view

urlpatterns = [
    path('etrot/', admin.site.urls),
    path('', include('Portal.urls')),
    path('selector/', include('selector.urls')),
    path('albam/', include('albam.urls')),
    path('birthday/', include('birthday.urls')),
    path('Natsumi/', RedirectView.as_view(url='/birthday/Natsumi/')),
    path('skmr/Natsumi/', RedirectView.as_view(url='/birthday/Natsumi/')),
    path('Kaoru/', RedirectView.as_view(url='/birthday/skmr/Kaoru/')),
    path('skmr/Kaoru/', RedirectView.as_view(url='/birthday/skmr/Kaoru')),
]
