from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaUno(request):
    html="""
    <h1 style="color:orange">Vista 1 App1</h1>
    """
    return HttpResponse(html)