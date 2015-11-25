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
import autocomplete_light.shortcuts as al


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/jsi18n', 'django.views.i18n.javascript_catalog'), 
    url(r'^$','prestamos.views.inicio'),
    url(r'^usuarios/page/(?P<pagina>.*)/$','prestamos.views.usuarios'),
    url(r'^usuarios/(?P<id_persona>.*)/$','prestamos.views.persona_individual'),
    url(r'^equipos/page/(?P<pagina>.*)/$','prestamos.views.equipos'),
    url(r'^equipos/(?P<id_equipo>.*)/$','prestamos.views.equipo_individual'),
    url(r'^add_persona/$','prestamos.views.add_persona'),
    url(r'^edit/persona/(?P<id_persona>.*)/$','prestamos.views.edit_persona'),
    url(r'^add_equipo/$','prestamos.views.add_equipo'),
    url(r'^edit/equipos/(?P<id_equipo>.*)/$','prestamos.views.edit_equipo'),
    url(r'^prestamos/page/(?P<pagina>.*)/$','prestamos.views.prestamos_historial'),
    url(r'^prestamos/(?P<id_prestamo>.*)/$','prestamos.views.prestamo_individual'),
    url(r'^prestamos_activos/page/(?P<pagina>.*)/$','prestamos.views.prestamos_activos'),
    url(r'^prestamos_activos/(?P<id_prestamo>.*)/$','prestamos.views.prestamo_activo_individual'),
    url(r'^add_prestamo/$','prestamos.views.add_prestamo'),
    url(r'^edit/prestamos_activos/(?P<id_prestamo>.*)/$','prestamos.views.edit_prestamo'),
    url(r'^close/prestamos_activos/(?P<id_prestamo>.*)/$','prestamos.views.close_prestamo'),
    url(r'^login/$','prestamos.views.login_view'), 
    url(r'^logout/$','prestamos.views.logout_view'),
    url(r'^auto/$','prestamos.views.lista_personas'), 
    #url(r'^usuarios/buscar/$','prestamos.views.buscar'), 

]
