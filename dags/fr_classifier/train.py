import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import os
import pickle

def train_and_save(train_csv: str) -> str:
    
    df = pd.read_csv(train_csv, header=0)
    X_train = df.drop('quality', axis=1) 
    Y_train = df['quality']
    classifier = RandomForestClassifier(random_state = 0, n_estimators = 100, criterion = 'entropy')
    classifier.fit(X_train,Y_train)
    filename = 'rf_classifier.pkl'


    # Directory where you want to save the .pkl file
    output_dir = './shared_data'
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

    # File path
    file_path = os.path.join(output_dir, filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    # Save the data to a .pkl file
    with open(file_path, 'wb') as f:
        pickle.dump(classifier, f)
