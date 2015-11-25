from django.shortcuts import render_to_response, get_object_or_404, render
from prestamos.models import Persona, Equipos, Prestamo, Rol, Estado_Equipo
from prestamos.forms import PersonaForm, EquiposForm, PrestamoForm, LoginForm, CloseForm
from prestamos import signals
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, m2m_changed
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth import login, logout, authenticate
from django.contrib import auth 
from django.contrib.auth.decorators import login_required
import json
#from django.utils import simplejson

# vistas consultas
def inicio(request):
	inicio = Persona.objects.all()
	return render_to_response('inicio.html',{'inicio':inicio})

#def buscar(requets):
#	return render_to_response('buscar.html')
#	 if request.is_ajax(): 
#		usuario = Persona.objects.filter(primer_apellido__startswith= request.GET['nombre'] ).values('nombre', 'id')) 
#	  	return HttpResponse( json.dumps(usuario), content_type='application/json' ) 
#	 else:
#	 	return HttpResponse("Solo Ajax")

@login_required(login_url='/login')
def usuarios(request,pagina):
	usuarios = Persona.objects.all().order_by('primer_apellido')

	paginator = Paginator(usuarios,10)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		list_usuarios = paginator.page(page)
	except (EmptyPage, InvalidPage):
		list_usuarios = paginator.page(paginator.num_pages)
	return render_to_response('usuarios.html',{'usuarios':list_usuarios})


#funcion para auttoccompletar formulario prestamo
def lista_personas(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = Persona.objects.filter(documento__icontains = q ).filter(estado='1')
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.id
            drug_json['label'] = str(drug.documento)+' ' + drug.primer_apellido + ' ' + drug.segundo_apellido + ' ' + drug.primer_nombre
            drug_json['value'] = drug.id
            results.append(drug_json)
        data = json.dumps(results)
        
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)



@login_required(login_url='/login')
def persona_individual(request,id_persona):
	persona = Persona.objects.get(id=id_persona)
	return render_to_response('persona_individual.html',{'persona':persona})

@login_required(login_url='/login')
def equipos(request,pagina):
	equipos = Equipos.objects.all()
	paginator = Paginator(equipos,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		list_equipo = paginator.page(page)
	except (EmptyPage, InvalidPage):
		list_equipo = paginator.page(paginator.num_pages)

	return render_to_response('equipos.html',{'equipos':list_equipo})

@login_required(login_url='/login')
def equipo_individual(request,id_equipo):
	equipo = Equipos.objects.get(id=id_equipo)
	return render_to_response('equipo_individual.html',{'equipo':equipo})

@login_required(login_url='/login')
def prestamos_activos(request,pagina):
	prestamos_activos = Prestamo.objects.filter(estado_prestamo=True).order_by('-id')
	paginator = Paginator(prestamos_activos,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		list_prestamos = paginator.page(page)
	except (EmptyPage, InvalidPage):
		list_prestamos = paginator.page(paginator.num_pages) 
	return render_to_response('prestamos_activos.html',{'prestamos_activos':list_prestamos})


@login_required(login_url='/login')
def prestamo_activo_individual(request,id_prestamo):
	prestamo = Prestamo.objects.get(id=id_prestamo)
	equipos = prestamo.equipos.all()
	return render_to_response('activo_individual.html',{'prestamo':prestamo,'equipos':equipos})


@login_required(login_url='/login')
def prestamos_historial(request,pagina):
	prestamos = Prestamo.objects.all().order_by('-id')
	paginator = Paginator(prestamos,3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		list_prestamos = paginator.page(page)
	except (EmptyPage, InvalidPage):
		list_prestamos = paginator.page(paginator.num_pages) 

	return render_to_response('prestamos.html',{'prestamos':list_prestamos})

@login_required(login_url='/login')
def prestamo_individual(request,id_prestamo):
	prestamo = Prestamo.objects.get(id=id_prestamo)
	equipos = prestamo.equipos.all()
	return render_to_response('prestamo_individual.html',{'prestamo':prestamo,'equipos':equipos})

#vistas para formularios
@login_required(login_url='/login')
def add_persona(request):
	if request.method=='POST':
		formulario = PersonaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios/page/1')
	else:
		formulario = PersonaForm()
	return render_to_response('personaform.html',{'formulario':formulario},context_instance=RequestContext(request))


@login_required(login_url='/login')
def edit_persona(request,id_persona):
	persona = Persona.objects.get(id=id_persona)
	
	if request.method == 'POST':
		formulario = PersonaForm(request.POST,instance=persona)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios/%s/'%persona.id)
	else:
		formulario = PersonaForm(instance=persona)
	

	return render_to_response('edit_personaform.html',{'formulario':formulario},context_instance=RequestContext(request))				


@login_required(login_url='/login')
def add_equipo(request):
	if request.method=='POST':
		formulario = EquiposForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/equipos/page/1')
	else:
		formulario = EquiposForm()
	return render_to_response('equiposform.html',{'formulario':formulario},context_instance=RequestContext(request))


@login_required(login_url='/login')
def edit_equipo(request,id_equipo):
	equipo = Equipos.objects.get(id=id_equipo)
	
	if request.method == 'POST':
		formulario = EquiposForm(request.POST,instance=equipo)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/equipos/%s/'%equipo.id)
	else:
		formulario = EquiposForm(instance=equipo)
	

	return render_to_response('edit_equiposform.html',{'formulario':formulario},context_instance=RequestContext(request))				



@login_required(login_url='/login')
def add_prestamo(request):
	
	if request.method=='POST':
		formulario = PrestamoForm(request.POST)
		
		if formulario.is_valid():
			formulario.save()
			
	            
		return HttpResponseRedirect('/prestamos_activos/page/1')

	else:
		formulario = PrestamoForm()
	return render_to_response('prestamoform.html',{'formulario':formulario},context_instance=RequestContext(request))

	


@login_required(login_url='/login')
def edit_prestamo(request,id_prestamo):
	prestamo = Prestamo.objects.get(id=id_prestamo)
	equipos = prestamo.equipos.all()
	if request.method == 'POST':
		formulario = PrestamoForm(request.POST,instance=prestamo)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/prestamos_activos/%s/'%prestamo.id)
	else:
		formulario = PrestamoForm(instance=prestamo)
	

	return render_to_response('edit_prestamoform.html',{'formulario':formulario},context_instance=RequestContext(request))				

def close_prestamo(request,id_prestamo):
	prestamo = Prestamo.objects.get(id=id_prestamo)
	equipos = prestamo.equipos.all()
	if request.method == 'POST':
		formulario = CloseForm(request.POST,instance=prestamo)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/prestamos_activos/%s/'%prestamo.id)
	else:
		formulario = CloseForm(instance=prestamo)
	

	return render_to_response('close_prestamoform.html',{'formulario':formulario},context_instance=RequestContext(request))				

	
def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/')
				else:
					mensaje = 'El usuario no se encuentra activo en el sistema'
			else:
				mensaje = "usuario y/o password incorrecto"
		else:
			mensaje = "usuario y/o password incorrecto"
	else:
		form = LoginForm()
	ctx = {'form':form,'mensaje':mensaje}
	return render_to_response('login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return 	HttpResponseRedirect('/login')