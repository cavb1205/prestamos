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
		fields = '__all__'