from django import forms
from .models import Solicitudes, Adjuntos

class AdjuntosForm(forms.ModelForm):
    class Meta:
        model = Adjuntos
        fields = ['archivo']

# Clase Solicitud donde el ciudadano captura la información de la solicitud para enviarla al sistema
class SolicitudForm(forms.ModelForm): 
    class Meta:
        # Se hace referencia al modelo Solicitudes situado en models.py, para enviar la información a la base de datos
        model = Solicitudes
        fields = ['titulo', 'lista_desplegable', 'fecha_reporte', 'descripcion']