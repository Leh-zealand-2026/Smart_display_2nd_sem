import openmeteo_requests
import requests_cache

from retry_requests import retry


def weather_code_name(code):
    code = int(code)

    if code == 0:
        return "Sunny"
    elif code in [1, 2]:
        return "Partly cloudy"
    elif code == 3:
        return "Cloudy"
    elif code in [45, 48]:
        return "Foggy"
    elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
        return "Rainy"
    elif code in [71, 73, 75]:
        return "Snowy"
    elif code == 95:
        return "Thunderstorm"
    else:
        return "Unknown"


def get_weather():
    cache_session = requests_cache.CachedSession(".cache", expire_after=1800)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 55.458,
        "longitude": 12.1821,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m",
            "weather_code",
        ],
        "wind_speed_unit": "ms",
        "timezone": "Europe/Copenhagen",
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    current = response.Current()

    current_temperature_2m = round(current.Variables(0).Value())
    current_relative_humidity_2m = round(current.Variables(1).Value())
    current_wind_speed_10m = round(current.Variables(2).Value(), 1)

    current_weather_code = int(current.Variables(3).Value())
    current_weather_text = weather_code_name(current_weather_code)

    weather = {
        "temperature": current_temperature_2m,
        "humidity": current_relative_humidity_2m,
        "wind_speed": current_wind_speed_10m,
        "weather_text": current_weather_text,
    }

    return weather

weather = get_weather()

print(f"Temperature: {weather['temperature']}°C")
print(f"Humidity: {weather['humidity']}%")
print(f"Wind speed: {weather['wind_speed']} m/s")
print(f"Weather: {weather['weather_text']}")