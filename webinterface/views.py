from django.shortcuts import render
from django.http import JsonResponse
from .API.open_meteo import get_weather
from .API.google_calendar import get_upcoming_events

# Create your views here.

def home(request):
    weather = get_weather()

    return render(request, "home.html", {
        "weather": weather
    })


def weather_api(request):
    weather = get_weather()
    return JsonResponse(weather)

def calendar_events(request):
    events = get_upcoming_events(max_results=10)
    return JsonResponse({"events": events})