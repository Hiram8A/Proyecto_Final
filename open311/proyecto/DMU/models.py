from django import models
from datetime import datetime
#from django.utils import timezone

#Modelo utilizado para los adjuntos opcionales. Se separó por cuestiones del valor a retornar
class Adjuntos(models.Model):
    archivo = models.FileField(upload_to='adjuntos/', null=True) #Se almacenan en la carpeta adjuntos/

SELECT_REQUEST_KIND = [
    ('Reporte de problema', 'Reporte de problema'),
    ('Solicitud de informacion', 'Solicitud de informacion')
]
class Solicitudes(models.Model):
    class Meta:
        verbose_name = 'Solicitudes' #Se asigna el nombre en singular y plural, para evitar doble "S" en la tabla de SQL
        verbose_name_plural = 'Solicitudes'

    # Título de la solicitud
    titulo = models.CharField("Título", max_length=300, default="Título de la solicitud a levantar") 
    # Sirve para indicar si es reporte o solicitud de información
    lista_desplegable = models.CharField("Tipo de solicitud", max_length=50, choices=SELECT_REQUEST_KIND, default="Reporte de problema")
    # Se asigna el valor de la fecha actual de forma automatica la del dia del reporte
    fecha_reporte = models.DateField("Fecha del reporte",  default=datetime.today)
    # Se describe de forma detallada el reporte o solicitud a levantar
    descripcion = models.CharField(max_length=500, default="Describa la solicitud a enviar") 
    # Archivos adjuntos opcionales, para agilizar la respuesta a la solicitud, y para fines de evidencia
    adjuntos = models.OneToOneField(Adjuntos, on_delete=models.CASCADE, null=True, blank=True)

    def _str_(self):
        return self.titulo