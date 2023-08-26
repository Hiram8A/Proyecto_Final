from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('home/', views.Inicio.as_view(), name= 'home' ),
    path('insertar/', views.insertar_solicitud, name='insertar' ),
    path('formulario/', views.Formulario.as_view(), name='formulario'),
    path('eliminar-solicitud/<int:solicitud_id>/', views.Eliminar_Solicitudes.as_view(),name='eliminar_solicitud'),
    path('estadisticas/', views.estadisticas_solicitudes, name='estadisticas_solicitudes')
] 