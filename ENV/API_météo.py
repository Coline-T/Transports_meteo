import requests
import csv
import time
import os

class WeatherClient:
    def __init__(self, api_key, lang='fr', units='metric'):
        """
        Initialise le client météo avec la clé API, la langue et les unités de mesure.
        """
        self.api_key = api_key
        self.lang = lang
        self.units = units
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, city_name):
        """
        Récupère les données météo pour la ville spécifiée.
        """
        params = {
            'q': city_name,
            'appid': self.api_key,
            'lang': self.lang,
            'units': self.units
        }

        try:
            # Effectuer la requête à l'API
            response = requests.get(self.base_url, params=params)
            data = response.json()

            # Vérifier si le statut de la réponse est correct (200 signifie succès)
            if response.status_code == 200:
                return data
            else:
                print(f"Erreur {data['cod']}: {data['message']}")
                return None
        except Exception as e:
            print(f"Erreur lors de la requête: {e}")
            return None

    def save_weather_to_csv(self, city_name, file_name='weather_data.csv'):
        """
        Enregistre les informations météo dans un fichier CSV pour une ville donnée.
        """
        data = self.get_weather_data(city_name)

        if data:
            try:
                # Extraire les informations météo
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                # Vérifier si le fichier existe déjà
                file_exists = os.path.isfile(file_name)

                # Ouvrir le fichier CSV en mode 'append' pour ajouter les données
                with open(file_name, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)

                    # Écrire l'en-tête si le fichier est vide ou n'existe pas
                    if not file_exists:
                        writer.writerow(
                            ["Ville", "Description", "Température (°C)", "Humidité (%)", "Vitesse du vent (m/s)"])

                    # Écrire les informations météo dans le fichier CSV
                    writer.writerow([city_name, weather_description, temperature, humidity, wind_speed])

                print(f"Les données météo pour {city_name} ont été enregistrées dans {file_name}.")

            except KeyError as e:
                print(f"Données manquantes dans la réponse : {e}")
        else:
            print("Impossible de récupérer les données météo.")

    def run(self, city_name, interval_hours=3):
        """
        Exécute la récupération et l'enregistrement des données toutes les X heures.
        """
        interval_seconds = interval_hours * 3600  # Conversion en secondes

        while True:
            self.save_weather_to_csv(city_name)
            print(f"Attente de {interval_hours} heure(s) avant la prochaine récupération...")
            time.sleep(interval_seconds)  # Attendre l'intervalle spécifié


# Utilisation de la classe WeatherClient

api_key = "b5db605ccc65331a910de85584bf4351"# Code de la clé API
weather_client = WeatherClient(api_key)# Initialisation du client météo
city_name = "Rennes"# Nom de la ville
weather_client.run(city_name, interval_hours=3)# Lancer le processus de récupération toutes les 3 heures

