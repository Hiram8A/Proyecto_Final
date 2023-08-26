from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
import json

def index(request):
    #request

    return HttpResponse("Hola mundo :P")

class Inicio(View):
    template_name = 'index.html'
    
    def post():
        '''Clase post'''
        return
    
    def get(self, request):
        '''
        Clase get
        '''
        print('Ha iniciado GET ---*')

        return render(request, self.template_name)
    