from django.shortcuts import render
from django.http import JsonResponse
from .API.open_meteo import get_weather

# Create your views here.

def home(request):
    weather = get_weather()

    return render(request, "home.html", {
        "weather": weather
    })


def weather_api(request):
    weather = get_weather()
    return JsonResponse(weather)