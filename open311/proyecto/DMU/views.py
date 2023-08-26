from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg

from .models import Solicitudes 
from .forms import SolicitudForm


def index(request):

    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'solicitudes.html'

    def post(self,request):

        return render(request,self.template_name)
    @method_decorator(login_required)


    def get(self,request):
        solicitudes = Solicitudes.objects.all()

        return render(request,self.template_name,{'solicitudes':solicitudes})
    
class Formulario(View):
    template_name = 'formulario.html'
    
    def post(self,request):
        form = SolicitudForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
        #else:
        #    JsonResponse("Se ha presentado un error")
            
        return render(request,self.template_name,{'form': form})

    def get(self,request):

        solicitudes = Solicitudes.objects.all()
        form = SolicitudForm()

        return render(request,self.template_name,{'form':form})

def insertar_solicitud(request):
    nueva_solicitud = Solicitudes(
        nombre = "Mazapan",
        descripcion = "Dulce de cacahuate",
        precio = 5,
        estatus = "True" 
    )
    nueva_solicitud.save()

    return HttpResponse("Solicitud Insertada Correctamente")

class Eliminar_Solicitudes(View):
    def post(self, request, solicitud_id):
        solicitud = get_object_or_404(Solicitudes, pk=solicitud_id)
        solicitud.delete()
        return redirect('home')
    
def estadisticas_solicitudes(request):
    # Obtener el Numero Total de Solicitudes disponibles
    total_solicitudes = Solicitudes.objects.aggregate(total_solicitudes=Sum('estatus'))['total_solicitudes'] 

    # Obtener el Año Más Reciente de Fecha de Registro
    max_fecha_registro = Solicitudes.objects.aggregate(max_fecha_registro=Max('fecha_registro'))['max_fecha_registro'] 

    # Obtener el Promedio de los Precios de Solicitudes
    promedio_precio = Solicitudes.objects.aggregate(promedio_precio=Avg('precio'))['promedio_precio']

    return render(request, 'estadisticas/estadisticas_solicitudes.html', {
        'total_solicitudes': total_solicitudes,
        'max_fecha_registro': max_fecha_registro,
        'promedio_precio': promedio_precio,
    })