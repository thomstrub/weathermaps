from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello WeatherMaps<h1>')

def about(request):
    return render(request, 'about.html')
def maps_index(request):
    return render(request, 'maps/index.html', {'maps': maps})
