import pickle
import numpy as np
from features import extract_features

model = pickle.load(open("model.pkl", "rb"))

def predict_genre(file_path):
    features = extract_features(file_path)
    features = features.reshape(1, -1)
    
    prediction = model.predict(features)
    return prediction[0]

print(predict_genre("test.wav"))