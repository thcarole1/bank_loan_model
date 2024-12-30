

def predict_house_price(number):
    # Retrieve housing data
    housing = load_housing_data()

    # Extract a specific number of rows
    housing_sample = housing.sample(number)

    # Create X (features) and y (target)
    X, y = create_x_y(housing_sample)

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
       say_hello()

    except:
        import sys
        import traceback
        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
