from django.shortcuts import render
from django.http import JsonResponse
from .API.open_meteo import get_weather
from .API.google_calendar import get_upcoming_events

# Create your views here.
# filled with temp information because system did not work after failing to pull weather api 1 day, despite working earlier.
def home(request):
    weather = {
        "temperature": "-",
        "weather_text": "Indlæser...",
        "humidity": "-",
        "wind_speed": "-"
    }

    return render(request, "home.html", {
        "weather": weather
    })


def weather_api(request):
    weather = get_weather()
    return JsonResponse(weather)

def calendar_events(request):
    events = get_upcoming_events(max_results=10)
    return JsonResponse({"events": events})