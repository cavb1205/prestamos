from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed

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


BOOL_CHOICES = ((True, 'Activo'),(False, 'Inactivo'))
class Persona(models.Model):
	codigo = models.IntegerField(null=True, blank=True, unique=True,verbose_name='Codigo')
	documento = models.IntegerField(unique=True,verbose_name='Documento')
	primer_nombre = models.CharField(max_length=30,verbose_name='Primer Nombre')
	segundo_nombre = models.CharField(max_length=30, blank=True, null=True,verbose_name='Segundo Nombre')
	primer_apellido = models.CharField(max_length=30,verbose_name='Primer Apellido')
	segundo_apellido = models.CharField(max_length=30,verbose_name='Segundo Apellido')
	email = models.EmailField(max_length=75)
	celular = models.CharField(max_length=13)
	programa = models.ForeignKey(Programa, blank=True, null=True)
	rol_id = models.ForeignKey(Rol,verbose_name='Rol')
	estado = models.BooleanField(default=True,choices=BOOL_CHOICES)
 

	def __unicode__(self):
		mostrar="%s - %s - %s - %s"%(self.primer_apellido,self.primer_nombre,self.documento, self.rol_id)
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

BOOL_CHOICES = ((True, 'Activo'),(False, 'Finalizado'))

class Prestamo(models.Model):
	id_persona = models.ForeignKey(Persona,verbose_name='Usuario')
	fecha_solicitud = models.DateTimeField(auto_now_add = True)
	fecha_prestamo = models.DateTimeField(auto_now_add = False,verbose_name='Fecha Prestamo')
	fecha_estimada_entrega = models.DateTimeField(null=True,blank=True, auto_now_add = False,verbose_name='Fecha Estimada de Entrega')
	salon = models.ForeignKey(Salon,null=True,blank=True,verbose_name='Salon')
	equipos = models.ManyToManyField(Equipos,verbose_name='Equipos')
	estado_prestamo = models.BooleanField(default=True, choices=BOOL_CHOICES,verbose_name='Estado del Prestamo')
	fecha_entrega = models.DateTimeField(null=True,blank=True,auto_now_add = False,verbose_name='Fecha de Entrega')
	observaciones = models.TextField(verbose_name='Observaciones sobre el prestamo',null=True, blank=True)



	def __unicode__(self):
		mostrar = "%s - %s - %s "%(self.fecha_solicitud, self.fecha_prestamo, self.fecha_entrega)
		return mostrar

#senales cambio estado de equipos

#@receiver(post_save, sender=Prestamo)
def prestamo_post_save(sender, instance, **kwargs):
	if instance.estado_prestamo == True:
		print 'Estado es Activo'
		for equipo in instance.equipos.all():
			equipo.estado_equipo_id = '2'
			equipo.save()
			print equipo.estado_equipo	
	else:
		print 'el estado es FINALIZADO'
		for equipo in instance.equipos.all():
			equipo.estado_equipo_id = '1'
			equipo.save()
			print equipo.estado_equipo		


	
m2m_changed.connect(prestamo_post_save, sender=Prestamo.equipos.through)


