from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Map

# class Map:
#     def __init__(self, name, region, subregion, elevation):
#         self.name = name
#         self.region = region
#         self.subregion = subregion
#         self.elevation = elevation

# maps = [
#     Map('Camp Muir', 'Paradise', 'Mt.Rainier', 8000),
#     Map('Mt. St. Helens South Ascent', 'Mt. St. Helens', 'South Cascades', 15000),
#     Map('Shipwreck Coast', 'Olympic Coast', 'Olympic Penninsula', 0)
# ]
class MapCreate(CreateView):
    model = Map
    fields ='__all__'
    success_url = '/maps/'

def home(request):
    return HttpResponse('<h1>Hello WeatherMaps<h1>')

def about(request):
    return render(request, 'about.html')

def maps_index(request):
    maps = Map.objects.all()
    return render(request, 'maps/index.html', {'maps': maps})
    
def maps_detail(request, map_id):
    map = Map.objects.get(id=map_id)
    return render(request, 'maps/detail.html', {'map': map})