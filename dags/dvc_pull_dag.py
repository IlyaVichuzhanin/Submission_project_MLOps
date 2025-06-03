from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='dvc_pull_dag',
    default_args=default_args,
    description='Pull data using DVC in Docker',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
    catchup=False,
) as dag:

    dvc_pull_task = DockerOperator(
        task_id='run_dvc_pull',
        image='my-dvc-image:latest',  # The image built earlier
        api_version='auto',
        command="dvc pull",
        mounts=[],  # Add volumes if needed for persistence
        environment={
            # Optional: set AWS keys or other env vars here
            "AWS_ACCESS_KEY_ID": "your_key",
            "AWS_SECRET_ACCESS_KEY": "your_secret"
        },
        network_mode="host"  # Optional: useful for local testing
    )

    dvc_pull_task