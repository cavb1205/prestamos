from django import forms
from django.forms import ModelForm
from models import Persona, Equipos

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'

class EquiposForm(forms.ModelForm):
	class Meta:
		model = Equipos 
		fields = '__all__'
	