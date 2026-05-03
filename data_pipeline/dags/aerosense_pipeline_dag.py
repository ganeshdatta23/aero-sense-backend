from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from data_pipeline.tasks.fetch_flight_data import fetch_flights
from data_pipeline.tasks.fetch_weather_data import fetch_weather
from data_pipeline.tasks.load_data_to_db import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'aerosense_ingestion_pipeline',
    default_args=default_args,
    description='AeroSense Flight & Weather Ingestion Pipeline',
    schedule_interval=timedelta(minutes=10),
    catchup=False,
) as dag:

    def ingest_flights_task():
        flights = fetch_flights()
        load_data("raw_flights", flights)
        return flights

    def ingest_weather_task(ti):
        # In a real scenario, we might sample a few flights or regions
        # For simplicity, we'll fetch weather for a fixed significant hub
        lat, lon = "40.6413", "-73.7781" # JFK Airport
        weather = fetch_weather(lat, lon)
        load_data("raw_weather", weather, lat=lat, lon=lon)

    fetch_flights_op = PythonOperator(
        task_id='fetch_flights',
        python_callable=ingest_flights_task,
    )

    fetch_weather_op = PythonOperator(
        task_id='fetch_weather',
        python_callable=ingest_weather_task,
    )

    fetch_flights_op >> fetch_weather_op
