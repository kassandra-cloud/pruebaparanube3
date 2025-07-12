from django.http import HttpResponse

def index(request):
    return HttpResponse("Actas funcionando correctamente")
from django.shortcuts import render

def index(request):
    return render(request, 'actas/index.html')
