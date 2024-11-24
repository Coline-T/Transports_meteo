import pandas as pd
import ast
import datetime as dt

file_path = 'C:/Users/solen/PycharmProjects/Transports_meteo/ENV/météo_data.csv'  # Remplacez par le chemin correct vers votre fichier
df_meteo = pd.read_csv(file_path, header=0)

new_df_transformed = pd.DataFrame()
for index, row in df_meteo.iterrows():
    new_row = {"temperature": [ast.literal_eval(row['main'])['temp']],
               "ressenti":[ast.literal_eval(row['main'])['feels_like']],
               "temp_min":[ast.literal_eval(row['main'])['temp_min']],
               "temp_max": [ast.literal_eval(row['main'])['temp_max']],
               "humidite": [ast.literal_eval(row['main'])['humidity']],
               }
    new_row = pd.DataFrame(new_row)
    new_df_transformed = pd.concat([new_df_transformed, new_row], ignore_index=True, axis=0)
df= df_meteo[['visibility','rain','dt_txt']]
# Extraction de la valeur associée à la clé '3H'
print(df['rain'].apply(type))

# Convertir les chaînes de caractères en dictionnaires si elles sont sous forme de chaînes
df['rain'] = df['rain'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Remplir les NaN avec {'3H': 0}
df['rain'] = df['rain'].apply(lambda x: {'3h': 0} if pd.isna(x) else x)

# Extraire la valeur associée à la clé '3H' dans le dictionnaire
df['rain'] = df['rain'].apply(lambda x: x['3h'] if isinstance(x, dict) else x)

# Vérification des types uniques dans la colonne
print(df['rain'].apply(type).unique())  # Afficher les types uniques dans la colonne
df_concat = pd.concat([df,new_df_transformed],axis=1)

# Convertir les colonnes Kelvin en Celsius
colonnes_a_convertir = ['temperature', 'ressenti', 'temp_min', 'temp_max']
for col in colonnes_a_convertir:
    df_concat[col] = df_concat[col] - 273.15

df_concat = df_concat.rename(columns={
    'visibility': 'visibilite',
    'rain':'pluie',
    'dt_txt': 'date'
})

# Forcer la conversion de la colonne 'date' en datetime
try:
    df_concat['date'] = pd.to_datetime(df_concat['date'], errors='coerce')  # Transforme en datetime, met NaT pour les valeurs non convertibles
    # Formater les dates au format %Y-%m-%d %H:%M:%S
    df_concat['date'] = df_concat['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
except Exception as e:
    print(f"Erreur pendant la conversion des dates : {e}")

# Réorganiser les colonnes dans l'ordre souhaité
ordre_colonnes = ['date', 'temperature', 'ressenti', 'temp_min', 'temp_max',
                 'humidite', 'pluie', 'visibilite']
df_concat = df_concat[ordre_colonnes]


# Sauvegarder le DataFrame transformé dans un nouveau fichier CSV
df_concat.to_csv('C:/Users/solen/PycharmProjects/Transports_meteo/ENV/météo_data_concat.csv',sep =";", index=False, date_format='%Y-%m-%d %H:%M:%S', quoting=1)

df_verif = pd.read_csv("C:/Users/solen/PycharmProjects/Transports_meteo/ENV/météo_data_concat.csv", sep= ";")
print(df_verif.head())
