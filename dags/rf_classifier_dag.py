from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from fr_classifier.data import prepare_data
from fr_classifier.train import train_and_save


file_path = 'data/winequality-red.csv'
train_file_path = 'data/winequality-red_train.csv'
model_file_path = 'fr_classifier/rf_classifier.pkl'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'rf_classifier',
    default_args=default_args,
    description='DAG для выгрузки данных и обучения модели random-forest на данных о вине',
    schedule=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['fr_classifier'],
) as dag:


    dvc_pull = BashOperator(
        task_id='dvc_pull',
        bash_command='cd /opt/airflow && dvc pull',
    )

    prepare_data_task = PythonOperator(
    task_id='prepare_data',
    python_callable= prepare_data,
    op_kwargs={'file_path': file_path},
    dag=dag,
    )

    train_and_save_model_task = PythonOperator(
    task_id='train_and_save_model_task',
    python_callable= train_and_save,
    op_kwargs={'train_csv': train_file_path},
    dag=dag,
    )

    dvc_pull >> prepare_data_task >> train_and_save_model_task