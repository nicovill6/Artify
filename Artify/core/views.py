from django.shortcuts import HttpResponse, render
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def instructores(request):
    return render(request, 'core/instructores.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def cursos(request):
    return render(request, 'core/cursos.html')
