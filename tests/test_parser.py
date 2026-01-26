import unittest
from weather_app.weather_parser import get_wind_direction


class TestWeatherParser(unittest.TestCase):

    def test_wind_direction(self):
        self.assertEqual(get_wind_direction(0), "N")
        self.assertEqual(get_wind_direction(90), "E")
        self.assertEqual(get_wind_direction(180), "S")
        self.assertEqual(get_wind_direction(270), "W")


if __name__ == "__main__":
    unittest.main()
