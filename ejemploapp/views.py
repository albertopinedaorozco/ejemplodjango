from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    respu = "<ul>"
    respu = respu + "<li>Elemento 1</li>"
    respu = respu + "<li>Elemento 2</li>"
    respu = respu + "</ul>"
    
    return HttpResponse(respu)

def nuevococinero(request):
    return HttpResponse("<p>Esta es la pagina de nuevo cocinero</p>")

def consultarpedidos(request):
    return HttpResponse("Consultar pedidos")
