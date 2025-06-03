# import sys
# sys.path.append("C:/Users/user/MyProjects/Intro_to_MLOps")
from fr_classifier.data import load_data, prepare_data
from fr_classifier.train import train_and_save
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator



default_dag_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

file_path = 'data/winequality-red.csv'
train_file_path = 'data/winequality-red_train.csv'
model_file_path = 'fr_classifier/rf_classifier.pkl'

dag = DAG(
    'random_forest',
    default_args=default_dag_args,
    schedule='@daily'
)

load_data_task = PythonOperator(
    task_id='load_data',
    python_callable= load_data,
    dag=dag,
)

prepare_data_task = PythonOperator(
    task_id='prepare_data',
    python_callable= prepare_data,
    op_kwargs={'csv_path': file_path},
    dag=dag,
)

train_and_save_model_task = PythonOperator(
    task_id='train_and_save_model_task',
    python_callable= train_and_save,
    op_kwargs={'train_csv': train_file_path},
    dag=dag,
)


load_data_task >> prepare_data_task >> train_and_save_model_task