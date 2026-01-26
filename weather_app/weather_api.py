import requests
import json
import time
from pathlib import Path
from typing import Optional, Dict, Tuple
from .config import API_KEY, CACHE_DURATION


class WeatherAPI:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "http://api.weatherapi.com/v1"
        self.cache_dir = Path("data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_path(self, key: str) -> Path:
        return self.cache_dir / f"{key}.json"

    def _get_cache(self, key: str) -> Optional[Dict]:
        path = self._cache_path(key)
        if path.exists() and time.time() - path.stat().st_mtime < CACHE_DURATION:
            with open(path) as f:
                return json.load(f)
        return None

    def _save_cache(self, key: str, data: Dict):
        with open(self._cache_path(key), "w") as f:
            json.dump(data, f)

    def _request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        params["key"] = self.api_key
        try:
            res = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=10)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            print("API Error:", e)
            return None

    def get_current(self, city: str) -> Tuple[Optional[Dict], str]:
        key = f"current_{city.lower()}"
        if cached := self._get_cache(key):
            return cached, "Using cached data"

        data = self._request("forecast.json", {"q": city, "days": 1})
        if data:
            self._save_cache(key, data)
            return data, "Live data"
        return None, "Error"

    def get_forecast(self, city: str) -> Tuple[Optional[Dict], str]:
        key = f"forecast_{city.lower()}"
        if cached := self._get_cache(key):
            return cached, "Using cached data"

        data = self._request("forecast.json", {"q": city, "days": 5})
        if data:
            self._save_cache(key, data)
            return data, "Live data"
        return None, "Error"
