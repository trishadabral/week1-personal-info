ICONS = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Snow": "❄️",
    "Thunderstorm": "⛈️",
    "Drizzle": "🌦️",
    "Mist": "🌫️"
}


def show_dashboard(current: dict, forecast: list, unit="C", cache_msg=None):
    print("\n🌤️  WEATHER DASHBOARD")
    print("=======================\n")

    print(f"📍 Current Location: {current['city']}, {current['country']}")
    print(f"🕐 Last Updated: {current['time']}\n")

    print("Current Weather:")
    print("────────────────")

    temp = current["temp"]
    feels = current["feels_like"]

    if unit == "F":
        temp = temp * 9/5 + 32
        feels = feels * 9/5 + 32

    print(f"Temperature:   {temp:.0f}°{unit} (Feels like: {feels:.0f}°{unit})")
    print(f"Conditions:    {current['condition']} {ICONS.get(current['icon'], '')}")
    print(f"Humidity:      {current['humidity']}%")
    print(f"Wind:          {current['wind_speed']} km/h from {current['wind_dir']}")
    print(f"Pressure:      {current['pressure']} hPa")
    print(f"Visibility:    {current['visibility']:.0f} km")
    print(f"Sunrise:       {current['sunrise']}")
    print(f"Sunset:        {current['sunset']}")

    print("\n5-Day Forecast:")
    print("───────────────")

    for day in forecast:
        min_t, max_t = day["min"], day["max"]
        if unit == "F":
            min_t = min_t * 9/5 + 32
            max_t = max_t * 9/5 + 32

        icon = ICONS.get(day["condition"], "")
        print(f"{day['date']}:  {icon}   {max_t:.0f}°{unit} / {min_t:.0f}°{unit}  (Humidity: {day['humidity']}%)")

    if cache_msg:
        print(f"\nAPI Status: {cache_msg}")

    print("Type 'refresh' to update, 'search' for new city, or 'quit' to exit:")
