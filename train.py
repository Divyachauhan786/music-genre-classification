import os
import numpy as np
from features import extract_features
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



X = []
y = []

data_path = "data/genres_original"

for genre in os.listdir(data_path):
    for file in os.listdir(os.path.join(data_path, genre)):
        file_path = os.path.join(data_path, genre, file)
        
        try:
            features = extract_features(file_path)
            X.append(features)
            y.append(genre)
        except Exception as e:
            print("Error with file:", file_path)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

print(os.listdir(data_path))

import pickle

pickle.dump(model, open("model.pkl", "wb"))