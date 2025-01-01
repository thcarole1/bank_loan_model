# Models
from xgboost import XGBClassifier

# Saving/loading models
import joblib

def get_model_api():
    '''
    Reloading the saved model
    '''
    final_model_reloaded = joblib.load("data/processed_data/my_bank_model.pkl")
    print("✅ model_api has been instantiated")
    return final_model_reloaded
