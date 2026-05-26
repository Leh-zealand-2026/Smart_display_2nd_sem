from django.shortcuts import render
from django.http import JsonResponse
from .API.open_meteo import get_weather
from .API.google_calendar import get_upcoming_events
import json
from django.views.decorators.http import require_http_methods, require_POST
from .API.notes_api import get_notes, add_note, remove_note

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
    try:
        weather = get_weather()
    except Exception as error:
        print("Kunne ikke hente data:", error)

        weather = {
            "temperature": "-",
            "weather_text": "Kunne ikke hente data from meteo weather api",
            "humidity": "-",
            "wind_speed": "-"
        }

    return JsonResponse(weather)

def calendar_events(request):
    events = get_upcoming_events(max_results=10)
    return JsonResponse({"events": events})

def notes_api(request):
    if request.method == "GET":
        notes = get_notes()
        return JsonResponse({"notes": notes})

    if request.method == "POST":
        data = json.loads(request.body)
        note = add_note(data.get("text", ""))

        if note is None:
            return JsonResponse({"error": "no blank notes"}, status=400)

        return JsonResponse(note)

def delete_note_api(request, note_id):
    deleted = remove_note(note_id)
    return JsonResponse({"deleted": deleted})