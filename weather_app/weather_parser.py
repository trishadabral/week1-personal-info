from datetime import datetime


def parse_current(data: dict) -> dict:
    current = data["current"]
    location = data["location"]
    forecast_day = data["forecast"]["forecastday"][0]

    return {
        "city": location["name"],
        "country": location["country"],
        "temp": current["temp_c"],
        "feels_like": current["feelslike_c"],
        "humidity": current["humidity"],
        "pressure": current["pressure_mb"],
        "visibility": current["vis_km"],
        "wind_speed": current["wind_kph"],
        "wind_dir": current["wind_dir"],
        "condition": current["condition"]["text"],
        "icon": current["condition"]["text"],
        "sunrise": forecast_day["astro"]["sunrise"],
        "sunset": forecast_day["astro"]["sunset"],
        "time": location["localtime"],
    }


def parse_forecast(data: dict) -> list:
    result = []

    for day in data["forecast"]["forecastday"]:
        result.append({
            "date": datetime.strptime(day["date"], "%Y-%m-%d").strftime("%a %d %b"),
            "min": day["day"]["mintemp_c"],
            "max": day["day"]["maxtemp_c"],
            "humidity": day["day"]["avghumidity"],
            "condition": day["day"]["condition"]["text"]
        })

    return result
