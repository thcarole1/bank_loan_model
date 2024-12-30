# Import from .py files
from ml_logic.data import load_banking_data
from ml_logic.model import get_model
from ml_logic.preprocessor import create_coordinates, \
                                rewrite_feature_names, \
                                create_x_y


def predict_bank_loan(number):
    # Retrieve banking data
    banking_data = load_banking_data()
    banking_data = rewrite_feature_names(banking_data)
    banking_data = create_coordinates(banking_data)

    # Extract a specific number of rows
    banking_data_sample = banking_data.sample(number)

    # Create X (features) and y (target)
    X, y = create_x_y(banking_data_sample)

    # Get the model to use
    final_model = get_model()

    # Predict
    predictions = final_model.predict(X)
    predictions = [round(prediction, 2) for prediction in predictions]
    print(predictions)

def say_hello():
    print('Hello World !')

if __name__ == '__main__':
    try:
        predict_bank_loan(10)

    except:
        import sys
        import traceback
        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
