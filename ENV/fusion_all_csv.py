import pandas as pd
import numpy as np
import os
import datetime
from dotenv import load_dotenv

from traitement_météo import ordre_colonnes

load_dotenv()

current_dir = 'C:\\Users\\solen\\PycharmProjects\\Transports_meteo\\ENV'
# chemin des fichiers
trafic_path = current_dir + '\\data\\transport.csv'
meteo_path= current_dir + '\\data\\meteo_data_concat.csv'

# lecture des fichiers
df_trafic = pd.read_csv(trafic_path , sep= ";")
df_meteo = pd.read_csv(meteo_path, sep =";")
df_meteo= df_meteo.rename(columns={"date":"datetime"})

# Réorganiser les colonnes dans l'ordre souhaité
#ordre_colonnes_m = ['date','time', 'temperature', 'ressenti', 'temp_min', 'temp_max',
 #                'humidite', 'pluie', 'visibilite']

#ordre_colonnes_t = ['_id',	'date','time','predefinedlocationreference','averagevehiclespeed','traveltime','traveltimereliability','trafficstatus',
     #               'vehicleprobemeasurement','geo_shape','gml_id','id_rva_troncon_fcd_v1_1','hierarchie','hierarchie_dv','denomination','insee',
      #              'sens_circule','vitesse_maxi','longitude','latitude']
#df_meteo = df_meteo[ordre_colonnes_m]

df_trafic['datetime'] = pd.to_datetime(df_trafic['datetime'], errors='coerce')
df_meteo['datetime'] = pd.to_datetime(df_meteo['datetime'], errors='coerce')
df_trafic = df_trafic.sort_values('datetime')
df_meteo = df_meteo.sort_values('datetime')

df_final = pd.merge_asof(left=df_trafic, right = df_meteo, on=['datetime'], direction = 'nearest', tolerance= pd.Timedelta('2H'))
# Remplir les NaN par "double sens"
df_final['sens_circule'] = df_final['sens_circule'].fillna('double sens')

df_final = df_final.drop('_id', axis=1)
df_final=df_final.dropna()
print(df_final)
# Sauvegarder le DataFrame transformé dans un nouveau fichier CSV
df_final.to_csv('C:/Users/solen/PycharmProjects/Transports_meteo/ENV/data/donnees_meteo_trafic.csv',sep =";", index=False, encoding = "utf-8-sig")