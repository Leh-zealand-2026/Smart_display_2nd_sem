from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/weather/", views.weather_api, name="weather_api"),
    path("api/calendar/", views.calendar_events, name="calendar_events"),
]