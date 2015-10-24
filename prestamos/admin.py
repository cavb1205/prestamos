from django.contrib import admin
from prestamos.models import Persona, Equipos, Prestamo, Rol, Programa, Estado_Equipo,Tipo_Equipo, Salon


# Register your models here.
admin.site.register(Persona)
admin.site.register(Equipos)
admin.site.register(Prestamo)
admin.site.register(Rol)
admin.site.register(Tipo_Equipo)
admin.site.register(Estado_Equipo)
admin.site.register(Salon)

admin.site.register(Programa)