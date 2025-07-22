from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.extract import extract
from src.transform import transform
from src.load import load

with DAG(
    dag_id="etl_dogs_api",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
) as dag:
    
    # Task 1 : extract
    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract,
        op_args=["https://api.thedogapi.com/v1/breeds"],
    )

    # Tasl 2 : transform
    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform,
        op_args=[extract_task.output],  # Usa el resultado de la tarea anterior
    )

    # Task 3 : load
    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load,
        op_args=[transform_task.output, "dogs"],
    )

    # Orden de ejecución
    extract_task >> transform_task >> load_task
