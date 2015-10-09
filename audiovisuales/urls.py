"""audiovisuales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','prestamos.views.inicio'),
    url(r'^usuarios/$','prestamos.views.usuarios'),
    url(r'^equipos/$','prestamos.views.equipos'),
    url(r'^add_persona/$','prestamos.views.add_persona'),
    url(r'^add_equipo/$','prestamos.views.add_equipo'),
    url(r'^prestamos/$','prestamos.views.prestamos'),
    url(r'^add_prestamo/$','prestamos.views.add_prestamo'),
]