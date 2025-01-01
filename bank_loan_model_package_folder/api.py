# Import libraries
from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd

# Import from api py files
from bank_loan_model_package_folder.api_functions.data_api import create_X
from bank_loan_model_package_folder.api_functions.model_api import get_model_api

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'New project': 'This is the first app of my new project !'}


@app.post("/predict")
def predict_func( Experience : int,
                    Income : int,
                    ZIP_Code : int,
                    Family : int,
                    CCAvg : float,
                    Education : int,
                    Mortgage : int,
                    Securities_Account : int,
                    CD_Account : int,
                    Online : int,
                    CreditCard : int):

    # Create X (features)
    X = create_X(Experience, Income, ZIP_Code, Family,
                    CCAvg, Education, Mortgage, Securities_Account,
                    CD_Account, Online, CreditCard)

    # Get the model to use
    final_model = get_model_api()

    # Predict
    prediction = final_model.predict(X)
    print("✅ predictions has been calculated")

    # Create a prediction dataframe
    predictions_df = pd.DataFrame({"prediction" : prediction})

    # Concatenate X and prediction as result
    result = pd.concat([X,predictions_df], axis = 1)

    result.to_json(path_or_buf = "data/processed_data/prediction_response.json")

    file_path = "data/processed_data/prediction_response.json"  # Path to your JSON file
    return FileResponse(file_path, media_type="application/json", filename="prediction_response.json")
