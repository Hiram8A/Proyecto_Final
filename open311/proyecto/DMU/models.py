from django.db import models
from datetime import datetime
# Create your models here.

#from django.utils import timezone

#Modelo Utilizado en caso de adjuntar (opcional), con sus respectivas selecciones
class Adjuntos(models.Model):
    archivo = models.FileField(upload_to='adjuntos/', null=True)

SELECT_REQUEST_KIND = [
    ('Reporte de problema', 'Reporte de problema'),
    ('Solicitud de informacion', 'Solicitud de informacion')
]
class Solicitudes(models.Model):
    class Meta:
        verbose_name = 'Solicitudes'           
        verbose_name_plural = 'Solicitudes'
        # Asignacion del nombre en singular y plural, para evitar doble "S" en la tabla de SQL.

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

    def __int__(self):
        return self.pk # Devuelve la PK relacionando las tabla y evitar crear modelos adicionales innecesarios