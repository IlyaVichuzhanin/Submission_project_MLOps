import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, r2_score, mean_absolute_error
import mlflow 
from mlflow.models import infer_signature
import joblib


mlflow.set_tracking_uri("http://127.0.0.1:8085")
experiment = mlflow.set_experiment("RandomForestClassifier")


if __name__ == "__main__":

    wine = pd.read_csv('data/winequality-red.csv')
    X = wine.drop('quality',axis=1)
    y=wine['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    classifier = RandomForestClassifier(random_state = 0, n_estimators = 100, criterion = 'entropy')
    
    with mlflow.start_run():

        classifier.fit(X_train, y_train)

        # Predicting Test Set
        y_pred = classifier.predict(X_test)

        signature = infer_signature(X_test, y_pred)

        accuracy = accuracy_score(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        mae=mean_absolute_error(y_true=y_test, y_pred=y_pred)
        

        mlflow.log_metric("accuracy_score", accuracy)
        mlflow.log_metric("r2_score", r2)
        mlflow.log_metric("mean_absolute_error", mae)
        

        mlflow.sklearn.log_model(
            sk_model=classifier,
            artifact_path="RandomForestClassifier",
            signature=signature,
            registered_model_name="RandomForestClassifier"
        )

