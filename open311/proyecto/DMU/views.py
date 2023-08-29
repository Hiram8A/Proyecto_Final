from django.http import HttpResponse
from django.views import View

from .models import Solicitudes     # Importacion de los modelos de Solicitudes 
from .forms import SolicitudForm

from django.shortcuts import render   #, redirect


def index(): 
    
    return HttpResponse("App de Solicitudes DMU") 

#Vista Inicio, para mostrar los elementos esenciales de interacción con la plataforma
class Inicio(View):
    template_name = 'inicio.html'
    
    def post(self, request): 
    
        return render(request, self.template_name) #Enviamos los elementos del template, para su almacenamiento
    
    def get(self, request):
        solicitudes = Solicitudes.objects.all() #Solicitamos todos los elementos del modelo Solicitudes
        
        return render(request, self.template_name, {'solicitudes': solicitudes})

#Vista Solicitud, para el envío de información de los ciudadanos
class Solicitud(View):
    template_name = 'solicitud.html'
    
    def post(self, request):
        form = SolicitudForm(request.POST) #Forma de Solicitud, con los datos de la solicitud del ciudadano
        if form.is_valid(): #Si la forma contiene todos los datos requeridos, guarda el registro en la base de datos
            solicitud = form.save()  # Guarda el objeto Solicitud y obtiene su referencia
            return render(request, self.template_name, {'form': form, 'solicitud': solicitud})
        return render(request, self.template_name, {'form': form})

    def get(self, request): #Regresa los datos de la solicitud, para fines de consulta y respuesta del servidor público
        form = SolicitudForm()
        return render(request, self.template_name, {'form': form})