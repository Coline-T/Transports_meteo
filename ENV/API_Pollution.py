import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime, timezone
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
        """Récupère les données météo pour une ville donnée en utilisant les coordonnées."""
        # Dictionnaire de coordonnées pour les villes
        city_coordinates = {
            "Rennes": (48.1173, -1.6778),
            # Ajoute d'autres villes si nécessaire
        }

        if city not in city_coordinates:
            print(f"Les coordonnées pour {city} ne sont pas disponibles.")
            return None

        lat, lon = city_coordinates[city]
        url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={self.api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'list' not in data or not data['list']:
                print(f"Aucune donnée de pollution pour {city}.")
                return None

            # Récupération des informations nécessaires
            air_quality_data = data['list'][0]

            # Formatage de la date et heure en format lisible
            date_time = datetime.fromtimestamp(air_quality_data['dt'], tz=timezone.utc).astimezone(self.timezone).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            return {
                "city": city,
                "date": date_time,
                "air_quality_index": air_quality_data['main']['aqi'],
                "components": {
                    "co": air_quality_data['components']['co'],
                    "no": air_quality_data['components']['no'],
                    "no2": air_quality_data['components']['no2'],
                    "o3": air_quality_data['components']['o3'],
                    "so2": air_quality_data['components']['so2'],
                    "pm2_5": air_quality_data['components']['pm2_5'],
                    "pm10": air_quality_data['components']['pm10'],
                    "nh3": air_quality_data['components']['nh3']
                }
            }
        else:
            print(f"Erreur pour {city}: {response.json().get('message')}")
            return None

    def display_weather_data(self):
        """Affiche les données météo sous forme de JSON."""
        print(json.dumps(self.weather_data, indent=4))


# Chargement de la clé API depuis le fichier .env
load_dotenv()
API_KEY = os.getenv('API_KEY_POLLUTION')

# Liste des villes
cities = [
    "Rennes",  # Bretagne
    # Ajoute d'autres villes ici si nécessaire
]

# Créer une instance de WeatherFetcher et récupérer les données météo
weather_fetcher = WeatherFetcher(cities, API_KEY)
weather_fetcher.fetch_weather_data()
weather_fetcher.display_weather_data()
