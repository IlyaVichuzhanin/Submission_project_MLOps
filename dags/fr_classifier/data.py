import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import subprocess
import os
import logging


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