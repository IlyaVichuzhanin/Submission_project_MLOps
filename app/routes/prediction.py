from fastapi import APIRouter, HTTPException
import pandas as pd
import joblib
import os


prediction_router = APIRouter(tags=['Prediction'])

@prediction_router.get('/get_prediction')
def get_prediction(
    fixed_acidity: float, 
    volatile_acidity: float, 
    citric_acid: float, 
    residual_sugar: float,
    chlorides: float,
    free_sulfur_dioxide: float,
    total_sulfur_dioxide: float,
    density: float,
    pH: float,
    sulphates: float,
    alcohol: float):

    try:
        data = {
            'fixed acidity': [fixed_acidity],
            'volatile acidity': [volatile_acidity],
            'citric acid': [citric_acid],
            'residual sugar':[residual_sugar],
            'chlorides':[chlorides],
            'free sulfur dioxide':[free_sulfur_dioxide],
            'total sulfur dioxide':[total_sulfur_dioxide],
            'density':[density],
            'pH':[pH],
            'sulphates':[sulphates],
            'alcohol':[alcohol]
        }

        df = pd.DataFrame(data)
        model_path = 'shared_data/rf_classifier.pkl'
        
        if not os.path.exists(model_path):
            raise HTTPException(status_code=404, detail="Model file not found")

        with open(model_path, 'rb') as file:
            model = joblib.load(file)

        prediction = model.predict(df)
        return {"predicted_quality": int(prediction[0])}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))