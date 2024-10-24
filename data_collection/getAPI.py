import requests

# URL de l'API
url = 'https://data.rennesmetropole.fr/api/explore/v2.1/catalog/datasets/etat-du-trafic-en-temps-reel/records?limit=50'

# Faire une requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Extraire les données au format JSON
    data = response.json()
    print("Données récupérées avec succès :")
    print(data)
else:
    print(f"Erreur lors de la requête : {response.status_code}")

class TrafficRecord:
    def __init__(self, datetime, location_id, avg_speed, travel_time, reliability, status):
        self.datetime = datetime
        self.location_id = location_id
        self.avg_speed = avg_speed
        self.travel_time = travel_time
        self.reliability = reliability
        self.status = status

    def __repr__(self):
        return f"TrafficRecord(datetime={self.datetime}, location={self.location_id}, status={self.status})"

class TrafficStatus:
    def __init__(self, status):
        valid_statuses = ['unknown', 'freeFlow', 'heavy', 'congested', 'impossible']
        if status in valid_statuses:
            self.status = status
        else:
            raise ValueError(f"Invalid traffic status: {status}")

    def __repr__(self):
        return self.status

# Exemple d'usage :
record = TrafficRecord(
    datetime="2024-10-24T10:30:00",
    location_id="12345_D",
    avg_speed=60,
    travel_time=120,
    reliability=95,
    status=TrafficStatus("freeFlow")
)

print(record)



