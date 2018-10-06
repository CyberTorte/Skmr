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
    path('etrotEhime/etrot/', admin.site.urls),
    path('etrotEhime/', include('Portal.urls')),
    path('etrotEhime/selector/', include('selector.urls')),
    path('etrotEhime/birthday/', include('birthday.urls')),
    path('etrotEhime/Natsumi/', RedirectView.as_view(url='/etrotEhime/birthday/Natsumi/')),
    path('etrotEhime/skmr/Natsumi/', RedirectView.as_view(url='/etrotEhime/birthday/Natsumi/')),
    path('etrotEhime/Kaoru/', RedirectView.as_view(url='/etrotEhime/birthday/skmr/Kaoru/')),
    path('etrotEhime/skmr/Kaoru/', RedirectView.as_view(url='/etrotEhime/birthday/skmr/Kaoru')),
]
