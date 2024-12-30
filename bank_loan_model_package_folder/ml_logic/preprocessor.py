# General library
import pandas as pd

# Geolocation libraries
import pgeocode
from geopy.geocoders import Nominatim

def rewrite_feature_names(df):
    # Updating the feature names for easier use.
    banking_data = df.rename(columns={
                                    "ZIP Code":"ZIP_Code",
                                    "Personal Loan":"Personal_Loan",
                                    "Securities Account":"Securities_Account",
                                    "CD Account": "CD_Account"
                                    })
    print("✅ Features have been renamed")
    return banking_data

def create_coordinates(df):
    # Retrieve geographical info from zip code
    ZIP_Codes = df['ZIP_Code'].values.astype('str').tolist()
    nomi = pgeocode.Nominatim('us')
    df_PostalCode = nomi.query_postal_code(ZIP_Codes)
    df_PostalCode['postal_code'] = df_PostalCode['postal_code'].values.astype('int64')
    # Remove duplicates
    df_PostalCode = df_PostalCode.drop_duplicates()

    # Create latitude and longitude columns
    banking_data = pd.merge(df,df_PostalCode[['postal_code', 'latitude', 'longitude']],
                        how='left',
                        left_on='ZIP_Code',
                        right_on='postal_code')

    # Dropping postal_code (not needed anymore)
    banking_data = banking_data.drop(columns='postal_code')
    print("✅ Coordinates have been created")
    return banking_data
