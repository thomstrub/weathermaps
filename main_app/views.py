from django.shortcuts import render
from django.http import HttpResponse

class Map:
    def __init__(self, name, region, subregion):
        self.name = name
        self.region = region
        self.subregion = subregion
        self.elevation = elevation

maps = [
    Map('Camp Muir', 'Paradise', 'Mt.Rainier', 8000),
    Map('Mt. St. Helens South Ascent', 'Mt. St. Helens', 'South Cascades', 15000),
    Map('Shipwreck Coast', 'Olympic Coast', 'Olympic Penninsula', 0)
]


def home(request):
    return HttpResponse('<h1>Hello WeatherMaps<h1>')

def about(request):
    return render(request, 'about.html')
def maps_index(request):
    return render(request, 'maps/index.html', {'maps': maps})
