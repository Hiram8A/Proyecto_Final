from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Va al archivo de views y busca a Index
    path('', views.index, name='index'),
    # Página de Home
    path('home/', views.Inicio.as_view(),name='home'),
    # Formulario para la creacion de solicitudes
    path('solicitud/', views.Solicitud.as_view(), name='solicitud'), 
    # Lista de Solicitudes Hechas por los Ciudadanos
    path('lista_solicitudes', views.lista_solicitudes.as_view(), name='lista_solicitudes'), 
]