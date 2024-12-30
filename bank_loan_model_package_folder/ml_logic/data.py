# Libraries to import data
import pandas as pd

def load_banking_data():
    # Retrieve the data stored locally
    path = "data/raw_data"
    banking_data = pd.read_excel(path + "/Bank_Personal_Loan_Modelling.xlsx", sheet_name="Data")
    print("✅ data has been loaded")
    return banking_data
