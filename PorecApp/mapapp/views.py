from django.shortcuts import render
from .models import Place
import json

def home(request):
    places = Place.objects.all()
    places_json = json.dumps([
        {
            "name": place.name,
            "description": place.description,
            "latitude": place.latitude,
            "longitude": place.longitude
        }
        for place in places
    ])
    return render(request, 'mapapp/home.html', {'places_json': places_json})
