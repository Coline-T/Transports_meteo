import requests
import csv
import time
import os

class AirPollutionClient:
    def __init__(self, api_key):
        """
        Initialise le client pollution de l'air avec la clé API.
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/air_pollution"

    def get_air_pollution_data(self, lat, lon):
        """
        Récupère les données de pollution de l'air pour la latitude et longitude spécifiées.
        """
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key
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

    def save_air_pollution_to_csv(self, lat, lon, city_name, file_name='air_pollution_data.csv'):
        """
        Enregistre les informations de pollution de l'air dans un fichier CSV pour une ville donnée.
        """
        data = self.get_air_pollution_data(lat, lon)

        if data:
            try:
                # Extraire les informations de pollution de l'air
                pollution_data = data['list'][0]['components']
                aqi = data['list'][0]['main']['aqi']

                # Vérifier si le fichier existe déjà
                file_exists = os.path.isfile(file_name)

                # Ouvrir le fichier CSV en mode 'append' pour ajouter les données
                with open(file_name, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)

                    # Écrire l'en-tête si le fichier est vide ou n'existe pas
                    if not file_exists:
                        writer.writerow([
                            "Ville", "AQI (Indice de qualité de l'air)", "CO (monoxyde de carbone)",
                            "NO (monoxyde d'azote)", "NO2 (dioxyde d'azote)", "O3 (ozone)",
                            "SO2 (dioxyde de soufre)", "PM2.5 (particules fines)", "PM10 (grosses particules)", "NH3 (ammoniac)"
                        ])

                    # Écrire les informations de pollution de l'air dans le fichier CSV
                    writer.writerow([
                        city_name, aqi, pollution_data['co'], pollution_data['no'], pollution_data['no2'],
                        pollution_data['o3'], pollution_data['so2'], pollution_data['pm2_5'], pollution_data['pm10'], pollution_data['nh3']
                    ])

                print(f"Les données de pollution de l'air pour {city_name} ont été enregistrées dans {file_name}.")

            except KeyError as e:
                print(f"Données manquantes dans la réponse : {e}")
        else:
            print("Impossible de récupérer les données de pollution de l'air.")

    def run(self, city_name, lat, lon, interval_hours=3):
        """
        Exécute la récupération et l'enregistrement des données de pollution de l'air toutes les X heures.
        """
        interval_seconds = interval_hours * 3600  # Conversion en secondes

        while True:
            self.save_air_pollution_to_csv(lat, lon, city_name)
            print(f"Attente de {interval_hours} heure(s) avant la prochaine récupération...")
            time.sleep(interval_seconds)  # Attendre l'intervalle spécifié


# Utilisation de la classe AirPollutionClient

api_key = "21cbcb7b2363369d509be3467eecb0ca"  # Nouvelle clé API
air_pollution_client = AirPollutionClient(api_key)  # Initialisation du client pollution de l'air
city_name = "Rennes"  # Nom de la ville
lat = 48.1173  # Latitude de Rennes
lon = -1.6778  # Longitude de Rennes
#air_pollution_client.run(city_name, lat, lon, interval_hours=1)  # Lancer le processus de récupération toutes les heures

air_pollution_client.get_air_pollution_data(lat, lon)