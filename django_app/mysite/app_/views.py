from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context 

def index(request):
  return render(request, 'index.html')

def form(request):
  return render(request, 'form.html')

def form_1(request):
  mensaje = "Artículo buscado: ", (request.GET["numero_1"])
  return HttpResponse(mensaje)