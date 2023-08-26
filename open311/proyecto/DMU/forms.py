#from typing import Any, Dict
from django import forms
from .models import Solicitudes

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['nombre','descripcion','precio','fecha_registro','estatus']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')             #Deben empatar con los atributos en mi modelo
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        fecha_registro = cleaned_data.get('fecha_registro')
        estatus = cleaned_data.get('estatus')

        if not nombre or not descripcion or not precio or not fecha_registro or not estatus:
            raise forms.ValidationError("Todos Los Campos Deben Ser Completados")
        return cleaned_data