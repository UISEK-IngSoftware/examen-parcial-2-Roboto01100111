from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Gore

# Create your views here.
def index(request):
    peliculas = Gore.objects.order_by('Nombre')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'Gore' : peliculas
    }, request))

def movies_details(request, id):
    pelicula = Gore.objects.get(id=id)
    template = loader.get_template('movies_details.html')
    return HttpResponse(template.render({ 'Gore' : pelicula}, request))