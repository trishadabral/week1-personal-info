from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import parse_current, parse_forecast
from weather_app.weather_display import show_dashboard

api = WeatherAPI()
unit = "C"
city = "London"

while True:
    raw_current, status1 = api.get_current(city)
    raw_forecast, _ = api.get_forecast(city)

    if raw_current and raw_forecast:
        current = parse_current(raw_current)
        forecast = parse_forecast(raw_forecast)
        show_dashboard(current, forecast, unit, cache_msg=status1)

    cmd = input("> ").lower()

    if cmd == "refresh":
        continue
    elif cmd == "search":
        city = input("Enter city name: ")
    elif cmd == "quit":
        break
    elif cmd == "unit":
        unit = "F" if unit == "C" else "C"
