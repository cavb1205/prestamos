from django.db import models

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
	codigo = models.IntegerField()
	documento = models.IntegerField()
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
		mostrar="%s - %s - %s - %s"%(self.codigo,self.primer_nombre,self.primer_apellido, self.rol_id)
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
	serial = models.CharField(max_length=30)
	estado_equipo = models.ForeignKey(Estado_Equipo)
	fecha_compra = models.DateField(auto_now=False)

	def __unicode__(self):
		mostrar  = "%s "%(self.nombre)
		return mostrar



class Prestamo(models.Model):
	id_persona = models.ForeignKey(Persona)
	fecha_solicitud = models.DateTimeField(auto_now_add = True)
	fecha_prestamo = models.DateTimeField(auto_now_add = False)
	fecha_entrega = models.DateTimeField(auto_now_add = False)

	def __unicode__(self):
		mostrar = "%s - %s - %s "%(self.fecha_solicitud, self.fecha_prestamo, self.fecha_entrega)
		return mostrar


class Det_Prestamo(models.Model):
	id_prestamo = models.ForeignKey(Prestamo)
	id_equipos = models.ForeignKey(Equipos)

	def __unicode__(self):
		mostrar = "%s - %s "%(self.id_prestamo, self.id_equipos)
		return mostrar



		


