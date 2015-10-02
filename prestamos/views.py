from django.shortcuts import render_to_response, get_object_or_404
from prestamos.models import Persona, Equipos, Prestamo, Rol
from django.template import RequestContext



# Create your views here.
def usuarios(request):
	usuarios = Persona.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios})

def equipos(request):
	equipos = Equipos.objects.all()
	return render_to_response('equipos.html',{'equipos':equipos})