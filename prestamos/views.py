from django.shortcuts import render_to_response, get_object_or_404
from prestamos.models import Persona, Equipos, Prestamo, Rol, Estado_Equipo
from prestamos.forms import PersonaForm, EquiposForm, PrestamoForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect



# vistas consultas
def inicio(request):
	inicio = Persona.objects.all()
	return render_to_response('inicio.html',{'inicio':inicio})


def usuarios(request):
	usuarios = Persona.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios})

def persona_individual(request,id_persona):
	persona = Persona.objects.get(id=id_persona)
	return render_to_response('persona_individual.html',{'persona':persona})



def equipos(request):
	equipos = Equipos.objects.all()
	return render_to_response('equipos.html',{'equipos':equipos})

def equipo_individual(request,id_equipo):
	equipo = Equipos.objects.get(id=id_equipo)
	return render_to_response('equipo_individual.html',{'equipo':equipo})



def prestamos(request):
	prestamos = Prestamo.objects.all()
	return render_to_response('prestamos.html',{'prestamos':prestamos})

def prestamo_individual(request,id_prestamo):
	prestamo = Prestamo.objects.get(id=id_prestamo)
	equipos = prestamo.equipos.all()
	return render_to_response('prestamo_individual.html',{'prestamo':prestamo,'equipos':equipos})
	


#vistas para formularios
def add_persona(request):
	if request.method=='POST':
		formulario = PersonaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else:
		formulario = PersonaForm()
	return render_to_response('personaform.html',{'formulario':formulario},context_instance=RequestContext(request))


def add_equipo(request):
	if request.method=='POST':
		formulario = EquiposForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/equipos')
	else:
		formulario = EquiposForm()
	return render_to_response('equiposform.html',{'formulario':formulario},context_instance=RequestContext(request))

def add_prestamo(request):
	
	if request.method=='POST':
		formulario = PrestamoForm(request.POST)
		if formulario.is_valid():
			formulario.save()

			return HttpResponseRedirect('/prestamos')

	else:
		formulario = PrestamoForm()
	return render_to_response('prestamoform.html',{'formulario':formulario},context_instance=RequestContext(request))