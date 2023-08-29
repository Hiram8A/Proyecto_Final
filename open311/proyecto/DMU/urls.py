from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'), #Va al archivo de views y busca index.Siempre llevan comas entre lineas
    path('home/', views.Inicio.as_view(),name='inicio'), #Página de inicio, muestra los botones esenciales si es que el usuario no se ha autenticado
    path('solicitud/', views.Solicitud.as_view(), name='solicitud'), #Formulario de solicitudes, relacionarlo a solicitud de views.py
]