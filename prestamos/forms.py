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
    
  class Meta:
  	model = Prestamo
  	fields = ('id_persona','fecha_prestamo','fecha_entrega','salon','equipos','estado_prestamo','observaciones')
  
  equipos = forms.ModelMultipleChoiceField(queryset=Equipos.objects.filter(estado_equipo='1'),widget=forms.CheckboxSelectMultiple)



	