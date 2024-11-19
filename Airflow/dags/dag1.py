# Import necessary libraries
from Airflow import DAG
from Airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
 
import subprocess
 
# Define a function to run the Python script
def run_trafic_api():
    # Path to your Python file
    script_path = 'C:\Users\cocop\Desktop\SUP DE VINCI\Entrepôt de données\Transports_meteo\data_collection\getAPI.py'
    # Using subprocess to run the Python script
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script : {e}")
 
 
# Define the DAG
dag = DAG(
    'Conso_API_dag',                 # DAG ID
    description='get data from the trafic API and load it in MongoDB',   # Description
    schedule_interval='0 */1 * * *',               # Schedule interval (runs once per hour) '@daily'
    start_date=datetime(2024, 1, 1),           # Start date (start running from this date)
    catchup=False                              # Whether to backfill missing DAG runs
)
 
run_trafic_api_task = PythonOperator(
    task_id='run_trafic_api',
    python_callable=run_trafic_api,             # Function to run
    dag=dag
)
 