from django import forms
from django.forms import ModelForm
from models import Persona, Equipos, Prestamo

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'

class EquiposForm(forms.ModelForm):
	class Meta:
		model = Equipos 
		fields = '__all__'

class PrestamoForm(forms.ModelForm):
  	equipos = forms.ModelMultipleChoiceField(queryset=Equipos.objects.filter(estado_equipo='1'))
  	class Meta:
  		model = Prestamo
  		fields = '__all__'

  	#id_persona = forms.ModelChoiceField(Persona.objects.all())
  	#fecha_prestamo = forms.DateTimeField()
  	#fecha_entrega = forms.DateTimeField()
  	#equipos = forms.ModelMultipleChoiceField(queryset=Equipos.objects.filter(estado_equipo='1'))



	