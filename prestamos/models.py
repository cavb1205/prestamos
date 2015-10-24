from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, m2m_changed
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, m2m_changed
# Create your models here.


class Programa(models.Model):
	nombre_programa = models.CharField(max_length=30)

	def __unicode__(self):
		mostrar = "%s "%(self.nombre_programa)
		return mostrar


class Rol(models.Model):
	rol = models.CharField(max_length=30)

	def __unicode__(self):
		mostrar = "%s "%(self.rol)
		return mostrar



class Persona(models.Model):
	codigo = models.IntegerField(null=True, blank=True, unique=True)
	documento = models.IntegerField(unique=True)
	primer_nombre = models.CharField(max_length=30)
	segundo_nombre = models.CharField(max_length=30, blank=True, null=True)
	primer_apellido = models.CharField(max_length=30)
	segundo_apellido = models.CharField(max_length=30)
	email = models.EmailField(max_length=75)
	celular = models.CharField(max_length=13)
	programa = models.ForeignKey(Programa, blank=True, null=True)
	rol_id = models.ForeignKey(Rol)
	estado = models.BooleanField(default=True)

	def __unicode__(self):
		mostrar="%s - %s - %s - %s"%(self.documento,self.primer_nombre,self.primer_apellido, self.rol_id)
		return mostrar

class Salon(models.Model):
	nombre = models.CharField(max_length=20)

	def __unicode__(self):
		mostrar = "%s"%(self.nombre)
		return mostrar


class Tipo_Equipo(models.Model):
	nombre_tipo_equipo = models.CharField(max_length=30)

	def __unicode__(self):
		mostrar  = "%s"%(self.nombre_tipo_equipo)
		return mostrar	



class Estado_Equipo(models.Model):
	nombre_estado_equipo=models.CharField(max_length=30)	

	def __unicode__(self):
		mostrar  = "%s"%(self.nombre_estado_equipo)
		return mostrar	


class Equipos(models.Model):
	nombre = models.CharField(max_length=30)
	tipo_equipo = models.ForeignKey(Tipo_Equipo) 
	descripcion = models.TextField(max_length=50)
	marca = models.CharField(max_length=30)
	modelo = models.CharField(max_length=30)
	serial = models.CharField(max_length=30, unique=True)
	estado_equipo = models.ForeignKey(Estado_Equipo)
	fecha_compra = models.DateField(null=True, blank=True, auto_now=False)

	def __unicode__(self):
		mostrar  = "%s "%(self.nombre)
		return mostrar



class Prestamo(models.Model):
	id_persona = models.ForeignKey(Persona)
	fecha_solicitud = models.DateTimeField(auto_now_add = True)
	fecha_prestamo = models.DateTimeField(auto_now_add = False)
	fecha_entrega = models.DateTimeField(null=True,blank=True, auto_now_add = False)
	salon = models.ForeignKey(Salon,null=True,blank=True)
	equipos = models.ManyToManyField(Equipos)
	estado_prestamo = models.BooleanField(default=True)
	observaciones = models.TextField(verbose_name='observaciones sobre el prestamo',null=True, blank=True)



	def __unicode__(self):
		mostrar = "%s - %s - %s "%(self.fecha_solicitud, self.fecha_prestamo, self.fecha_entrega)
		return mostrar


	
	#@receiver(post_save, sender = Prestamo)
	#def prestamo_save(sender, instance, **kwargs):
	#	for equipo in instance.equipos:
	#		equipo.estado_equipo = '2'
	#		equipo.save()
			


