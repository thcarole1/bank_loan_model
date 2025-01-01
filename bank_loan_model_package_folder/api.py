# Import libraries
from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd

# Import from api py files
from bank_loan_model_package_folder.api_functions.data_api import create_X

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

    return ''
