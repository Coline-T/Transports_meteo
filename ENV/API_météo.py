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
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Récupérer la date actuelle et convertir le timestamp en UTC
            current_datetime = datetime.now().astimezone(self.timezone).strftime("%Y-%m-%d %H:%M:%S")

            # Transformation des données pour structurer les informations nécessaires
            weather_data = [
                {
                    'timestamp': datetime.fromtimestamp(entry['dt'], tz=timezone.utc),  # Convertir en UTC
                    'temperature': entry['main']['temp'] - 273.15,  # Conversion en °C
                    'feels_like': entry['main']['feels_like'] - 273.15,  # Température ressentie en °C
                    'temp_min': entry['main']['temp_min'] - 273.15,  # Température minimale en °C
                    'temp_max': entry['main']['temp_max'] - 273.15,  # Température maximale en °C
                    'pressure': entry['main']['pressure'],  # Pression atmosphérique
                    'humidity': entry['main']['humidity'],  # Humidité
                    'weather_description': entry['weather'][0]['description'],
                    # Description de la météo (par ex. "clear sky")
                    'wind_speed': entry['wind']['speed'],  # Vitesse du vent
                    'wind_deg': entry['wind']['deg'],  # Direction du vent (en degrés)
                    'wind_gust': entry['wind'].get('gust', None),  # Rafales de vent (optionnel)
                    'visibility': entry['visibility'],  # Visibilité
                    'clouds': entry['clouds']['all'],  # Couverture nuageuse
                    'timestamp_readable': entry['dt_txt']  # Heure lisible
                }
                for entry in data.get('list', [])
            ]

            # Structuration de la réponse
            return {
                "city": data['city']['name'],
                "country": data['city']['country'],
                "date": current_datetime,
                "weather_data": weather_data  # Liste de données météo détaillées
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
