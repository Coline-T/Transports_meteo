from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Définir les arguments par défaut du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 1),  # Ajustez la date de début
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Définir le DAG
dag = DAG(
    'meteo_kafka_dag',
    default_args=default_args,
    description='Température météo et humidité',
    schedule_interval='0 */3 * * *',  # Exécution toutes les 8 heures
)


# Fonction pour exécuter le script sentiment_analysis.py
def run_meteo():
    try:
        subprocess.run(['python3',
                        'C:/Users/solen/PycharmProjects/Transports_meteo/ENV/API_météo.py'],
                       check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script : {e}")


# Définir la tâche pour exécuter le script Python
run_meteo_task = PythonOperator(
    task_id='run_meteo',
    python_callable=run_meteo,
    dag=dag,
)