from django.shortcuts import render_to_response, get_object_or_404
from prestamos.models import Persona, Equipos, Prestamo, Rol
from prestamos.forms import PersonaForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect



# vistas consultas
def usuarios(request):
	usuarios = Persona.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios})

def equipos(request):
	equipos = Equipos.objects.all()
	return render_to_response('equipos.html',{'equipos':equipos})


#vistas para formularios
def nueva_persona(request):
	if request.method=='POST':
		formulario = PersonaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else:
		formulario = PersonaForm()
	return render_to_response('personaform.html',{'formulario':formulario},context_instance=RequestContext(request))
