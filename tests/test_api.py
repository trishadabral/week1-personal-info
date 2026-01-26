import unittest
from weather_app.weather_api import WeatherAPI


class TestWeatherAPI(unittest.TestCase):

    def setUp(self):
        self.api = WeatherAPI()

    def test_cache_path(self):
        path = self.api._cache_path("test_city")
        self.assertTrue(str(path).endswith("test_city.json"))

    def test_cache_write_and_read(self):
        key = "unit_test"
        sample_data = {"test": "data"}

        self.api._save_cache(key, sample_data)
        cached = self.api._get_cache(key)

        self.assertEqual(cached, sample_data)


if __name__ == "__main__":
    unittest.main()
