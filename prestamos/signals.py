#from django.db.models.signals import post_save
#from django.dispatch import receiver, Signals 
#from prestamos.models import Prestamo



#@receiver(post_save, sender = Prestamo)
#	def prestamo_save(sender, instance, **kwargs):
#		for equipo in instance.equipos:
#			equipo.estado_equipo = 'Ocupado'
#			equipo.save()
	