from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Solicitudes     # Importacion de los modelos de Solicitudes 
from .forms import SolicitudForm

def index(): 
    
    return HttpResponse("App de Solicitudes DMU") 

# Vista de la Pantalla de Inicio
class Inicio(View):
    template_name = 'home.html'
    
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
    
class lista_solicitudes(View):
    template_name = 'lista_solicitudes.html'

    def post(self,request):

        return render(request,self.template_name)
    @method_decorator(login_required)


    def get(self,request):
        solicitudes = Solicitudes.objects.all()

        return render(request,self.template_name,{'solicitudes':solicitudes})