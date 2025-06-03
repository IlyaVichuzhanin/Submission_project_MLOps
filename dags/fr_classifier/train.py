import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import os

def train_and_save(train_csv: str) -> str:
    
    df = pd.read_csv(train_csv, header=0)
    X_train = df.drop('quality', axis=1) 
    Y_train = df['quality']
    classifier = RandomForestClassifier(random_state = 0, n_estimators = 100, criterion = 'entropy')
    classifier.fit(X_train,Y_train)
    filename = 'rf_classifier.pkl'
    
    if os.path.exists(filename):
        os.remove(filename)

    joblib.dump(classifier, filename=filename)