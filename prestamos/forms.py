from django import forms
from django.forms import ModelForm
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
  	fields = ('id_persona','fecha_prestamo','fecha_estimada_entrega','salon','equipos','estado_prestamo','fecha_entrega','observaciones')
  	widgets = {
  		'estado_prestamo':forms.Select,  'fecha_entrega':forms.SplitDateTimeWidget(date_format='%d/%m/%Y')
  	}

  def __init__(self, *args, **kwargs):
       super(PrestamoForm, self).__init__(*args, **kwargs)
       self.fields['fecha_prestamo'].widget = widgets.AdminSplitDateTime()
       self.fields['fecha_estimada_entrega'].widget = widgets.AdminSplitDateTime()
       self.fields['fecha_entrega'].widget = widgets.AdminSplitDateTime()
       self.fields['id_persona'].queryset = Persona.objects.filter(estado='1').order_by('primer_apellido')

        
  equipos = forms.ModelMultipleChoiceField(queryset=Equipos.objects.filter(estado_equipo='1'),widget=forms.CheckboxSelectMultiple)



	