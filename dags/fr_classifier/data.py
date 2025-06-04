import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import subprocess
import os
import logging


def load_data():
    try:
        result = subprocess.run(
            [f"/home/airflow/.local/bin/dvc", "pull"],
            capture_output=True,
            text=True,
            check=True
        )
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("Command failed with error:")
        print(e.stderr)
        raise

    # logger = logging.getLogger(__name__)

    # try:
    #     result = subprocess.run(['dvc', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #     if result.returncode == 0:
    #         logger.info("✅ DVC доступен в PATH.")
    #         print("✅ DVC доступен в PATH.")
    #         print("Версия DVC:", result.stdout.strip())
    #     else:
    #         print("❌ DVC не установлен глобально.")
    #         logger.info("❌ DVC не установлен глобально.")
    # except FileNotFoundError:
    #     print("❌ DVC не найден в PATH.")
    #     logger.info("❌ DVC не найден в PATH.")
    

    # logger = logging.getLogger(__name__)
    
    # # Проверка текущей директории
    # current_dir = os.getcwd()
    # logger.info(f"Current directory: {current_dir}")
    
    # try:
    #     # Проверка PATH
    #     path = os.environ.get("PATH")
    #     logger.info(f"PATH: {path}")
        
    #     # Проверка наличия dvc в PATH
    #     result = subprocess.run(
    #         ["which", "dvc"],
    #         capture_output=True,
    #         text=True,
    #         check=True
    #     )
    #     logger.info(f"dvc found at: {result.stdout.strip()}")
        
    #     # Выполнение dvc pull
    #     result = subprocess.run(
    #         ["dvc", "pull"],
    #         capture_output=True,
    #         text=True,
    #         check=True
    #     )
        
    #     logger.info("dvc pull completed successfully.")
    #     logger.debug(f"Output: {result.stdout}")
    #     logger.debug(f"Errors: {result.stderr}")
    # except subprocess.CalledProcessError as e:
    #     logger.error(f"Command failed with error: {e}")
    #     logger.error(f"Output: {e.output}")
    #     logger.error(f"Errors: {e.stderr}")
    #     raise


    
















    


def prepare_data(file_path:str) -> pd.DataFrame:
    
    wine = pd.read_csv(file_path)
    X = wine.drop('quality',axis=1)
    y=wine['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    train_df = pd.concat([X_train, y_train], axis=1)
    test_df = pd.concat([X_test, y_test], axis=1)

    train_file_path = 'data/winequality-red_train.csv'
    test_file_path = 'data/winequality-red_test.csv'

    if os.path.exists(train_file_path):
        os.remove(train_file_path)

    if os.path.exists(test_file_path):
        os.remove(test_file_path)

    train_df.to_csv(train_file_path, index=False)
    test_df.to_csv(test_file_path, index=False)

    return wine