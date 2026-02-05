import requests

WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

API_URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": 52.3676,
    "longitude": 4.9041,
    "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
}


def get_weather():
    """Fetch current weather data for Amsterdam from Open-Meteo API."""
    response = requests.get(API_URL, params=PARAMS, timeout=10)
    response.raise_for_status()
    data = response.json()

    current = data["current"]
    weather_code = current["weather_code"]

    return {
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "condition": WMO_CODES.get(weather_code, f"Unknown ({weather_code})"),
    }


if __name__ == "__main__":
    try:
        weather = get_weather()
        print("Current weather in Amsterdam:")
        print(f"  Temperature: {weather['temperature']}°C")
        print(f"  Condition:   {weather['condition']}")
        print(f"  Humidity:    {weather['humidity']}%")
        print(f"  Wind speed:  {weather['wind_speed']} km/h")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to weather service.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP {e.response.status_code} from weather service.")
    except requests.exceptions.JSONDecodeError:
        print("Error: Invalid response from weather service.")
    except KeyError as e:
        print(f"Error: Missing expected data in response: {e}")
