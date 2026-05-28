from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/weather/", views.weather_api, name="weather_api"),
    path("api/calendar/", views.calendar_events, name="calendar_events"),
    path("api/notes/", views.notes_api, name="notes_api"),
    path("api/notes/<int:note_id>/delete/", views.delete_note_api, name="delete_note_api"),
    path("api/alarm-buzzer/", views.alarm_buzzer_api, name="alarm_buzzer_api"),
]