import os
from pymongo import MongoClient
from pandas import DataFrame
from dotenv import load_dotenv
import pandas as pd

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer l'URI de MongoDB à partir de la variable d'environnement
MONGO_URI = os.getenv('MONGO_URI')

# Vérifier que l'URI est correctement chargé
if MONGO_URI is None:
    raise ValueError("La variable d'environnement MONGO_URI n'est pas définie.")

# Connexion à MongoDB
client = MongoClient(MONGO_URI)
db = client['Environnement-db']  # Remplace par le nom de ta base de données
collection = db['Météo']  # Remplace par le nom de ta collection

# Récupérer les documents de la collection
documents = collection.find({})  # Vous pouvez ajouter un filtre si nécessaire

# Extraire la partie `list`
list_data = []
for document in documents:
    list_data.extend(document["list"])  # Ajouter les éléments de `list` dans la liste
# Créer un DataFrame pandas pour le CSV
df = pd.DataFrame(list_data)


# Déterminer le chemin pour sauvegarder le fichier CSV
current_dir = os.getcwd()
end_path = os.path.join(current_dir, "data")  # Utilisation de os.path.join pour gérer le chemin
end_file = os.path.join(end_path, 'météo_data.csv')

# Afficher le chemin du fichier
print(end_file)

# Exporter vers un fichier CSV
df.to_csv("météo_data.csv",sep = ";", index=False)
