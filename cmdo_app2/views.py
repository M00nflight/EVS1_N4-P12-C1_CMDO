from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaDos(request):
    html="""
    <h1 style="color:blue">Vista 1 App2</h1>
    <body><h1>Vista 2</h1><p>Este es el contenido de la vista dos.</p></body>
    <img src="https://i.pinimg.com/564x/ba/01/72/ba017251aeb2ecac1f576fee21b40b93.jpg"/>
    """
    return HttpResponse(html)