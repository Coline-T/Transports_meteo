import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import pytz


class WeatherFetcher:
    def __init__(self, cities, api_key, timezone="Europe/Paris"):
        self.cities = cities
        self.api_key = api_key
        self.timezone = pytz.timezone(timezone)
        self.weather_data = []

    def fetch_weather_data(self):
        """Récupère les données météo pour chaque ville."""
        for city in self.cities:
            data = self._get_city_weather(city)
            if data:
                self.weather_data.append(data)
        return self.weather_data

    def _get_city_weather(self, city):
        """Récupère les données météo pour une ville donnée et retourne un dictionnaire avec les informations nécessaires."""
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            current_datetime = datetime.now().astimezone(self.timezone).strftime("%Y-%m-%d %H:%M:%S")
            return {
                "city": data['name'],
                "date": current_datetime,
                "temperature": data['main']['temp'] - 273.15,  # Conversion en °C
                "humidity": data['main']['humidity']
            }
        else:
            print(f"Erreur pour {city}: {data.get('message')}")
            return None

    def display_weather_data(self):
        """Affiche les données météo sous forme de JSON."""
        print(json.dumps(self.weather_data, indent=4))


load_dotenv()
API_KEY = os.getenv('API_KEY_MET')

cities = [
    "Rennes",  # Bretagne
]

# Créer une instance de WeatherFetcher et récupérer les données météo

weather_fetcher = WeatherFetcher(cities, API_KEY)
weather_fetcher.fetch_weather_data()
weather_fetcher.display_weather_data()
