from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaUno(request):
    html="""
    <h1 style="color:orange">Vista 1 App1</h1>
    <body><h1>Vista 2</h1><p>Este es el contenido de la vista uno.</p></body>
        <style>
        .parrafo-con-fondo {
            background-color: #FFA500; 
            padding: 10px;
        }
    </style>
    <p class="parrafo-con-fondo">Este es un párrafo con un color de fondo naranja.</p>
    <img src="https://i.pinimg.com/564x/72/1f/71/721f71843f692f511a03f30a47d2764f.jpg" />

    """
    return HttpResponse(html)