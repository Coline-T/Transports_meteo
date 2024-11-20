# Import necessary libraries
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

import subprocess


# Define a function to run the Python script
def run_meteo_api():
    # Path to your Python file
    script_path = 'C:/Users/solen/PycharmProjects/Transports_meteo/ENV/API_météo.py'
    # Using subprocess to run the Python script
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script : {e}")


# Define the DAG
dag = DAG(
    'Conso_API_dag',  # DAG ID
    description='get data from OpenWeather API and load it in MongoDB',  # Description
    schedule_interval='0 0 */5 * *',  # Exécute tous les 5 jours à minuit
    start_date = datetime.today(),
    catchup=False  # Whether to backfill missing DAG runs
)

run_meteo_api_task = PythonOperator(
    task_id='run_meteo_api',
    python_callable=run_meteo_api,  # Function to run
    dag=dag
)