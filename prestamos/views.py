from django.shortcuts import render_to_response, get_object_or_404
from prestamos.models import Persona, Equipos, Prestamo, Rol, Estado_Equipo
from prestamos.forms import PersonaForm, EquiposForm, PrestamoForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, m2m_changed

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


def prestamos_activos(request):
	prestamos_activos = Prestamo.objects.filter(estado_prestamo=True).order_by('-id')
	return render_to_response('prestamos_activos.html',{'prestamos_activos':prestamos_activos})

def prestamo_activo_individual(request,id_prestamo):
	prestamo = Prestamo.objects.get(id=id_prestamo)
	equipos = prestamo.equipos.all()
	return render_to_response('activo_individual.html',{'prestamo':prestamo,'equipos':equipos})


def prestamos_historial(request):
	prestamos = Prestamo.objects.all().order_by('-id')
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
		#equipo_afectado_id=request.POST.equipos_id
		if formulario.is_valid():
			formulario.save()
		#	Equipos.update(pk=equipo_afectado_id,Estado_Equipo='Ocupado')
			
			return HttpResponseRedirect('/prestamos_activos')

	else:
		formulario = PrestamoForm()
	return render_to_response('prestamoform.html',{'formulario':formulario},context_instance=RequestContext(request))

	@receiver(post_save, sender = Prestamo)
	def prestamo_save(sender, instance, **kwargs):
		for equipo in instance.equipos:
			equipo.estado_equipo = '2'
			equipo.save()
				
	#post_save.connect(prestamo_save, sender = Prestamo)		

