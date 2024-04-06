import pickle

# Load the trained model
with open('model.pkl', 'rb') as file:
    lr_sklearn = pickle.load(file)

def predict(value):
    """
    Function to make predictions using the loaded model.
    """
    predicted_value = lr_sklearn.predict([[value]])
    return predicted_value[0][0]