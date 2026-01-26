import unittest
from weather_app.weather_display import ICONS


class TestWeatherDisplay(unittest.TestCase):

    def test_icons_exist(self):
        self.assertIn("Clear", ICONS)
        self.assertIn("Rain", ICONS)
        self.assertIn("Clouds", ICONS)


if __name__ == "__main__":
    unittest.main()
