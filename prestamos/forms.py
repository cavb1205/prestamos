from django import forms
import autocomplete_light
from django.forms import ModelForm, Textarea
from models import Persona, Equipos, Prestamo
from django.contrib.admin import widgets
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'
   # widgets = {
    #  'codigo':forms.TextInput(attrs={'class': 'form-group'})
    #}

class EquiposForm(forms.ModelForm):
	class Meta:
		model = Equipos 
		fields = '__all__'

class PrestamoForm(forms.ModelForm):
  class Meta:
  	model = Prestamo
  
  	fields = ('id_persona','fecha_prestamo','fecha_estimada_entrega','salon','equipos')
  	widgets = {
 	
      'estado_prestamo':forms.Select,'observaciones':forms.Textarea(attrs={'class':'form-inline'}), 'fecha_prestamo':forms.DateTimeInput(attrs={'id':'fecha_prestamo'}),'fecha_estimada_entrega':forms.DateTimeInput(attrs={'id':'fecha_estimada_entrega'}) ,'fecha_entrega':forms.DateTimeInput(attrs={'id':'fecha_entrega'}),'id_persona' : forms.TextInput(attrs={'id':'tags'})
  	}

  def __init__(self, *args, **kwargs):
       super(PrestamoForm, self).__init__(*args, **kwargs)
       ####filtro usuario en formulario para moostrar slo los activos y ordenados por apellidos
       #self.fields['id_persona'].queryset = Persona.objects.filter(estado='1').order_by('primer_apellido')
       

        
  equipos = forms.ModelMultipleChoiceField(queryset=Equipos.objects.filter(estado_equipo='1'),widget=forms.CheckboxSelectMultiple)


class CloseForm(forms.ModelForm):
  class Meta:
    model = Prestamo
  
    fields = ('estado_prestamo','fecha_entrega','observaciones','equipos')
    widgets = {
  
      'estado_prestamo':forms.Select,'observaciones':forms.Textarea(attrs={'class':'form-inline'}),'fecha_entrega':forms.DateTimeInput(attrs={'id':'fecha_entrega'}) 
    }
  
        
  equipos = forms.ModelMultipleChoiceField(queryset=Equipos.objects.all(),widget=forms.CheckboxSelectMultiple)
  

	