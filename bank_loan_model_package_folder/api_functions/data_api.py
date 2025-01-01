import pandas as pd

def create_X(Experience : int, Income : int, ZIP_Code : int,\
            Family : int, CCAvg : float, Education : int,\
            Mortgage : int, Securities_Account : int,\
            CD_Account : int, Online : int,CreditCard : int):

    dict = {"Experience" : Experience,
            "Income" : Income,
            "ZIP_Code" : ZIP_Code,
            "Family" : Family,
            "CCAvg" : CCAvg,
            "Education" : Education,
            "Mortgage" : Mortgage,
            "Securities_Account" : Securities_Account,
            "CD_Account" : CD_Account,
            "Online" : Online,
           "CreditCard" : CreditCard}
    df = pd.DataFrame(dict, index = [0])
    print("✅ X has been created")
    return df
