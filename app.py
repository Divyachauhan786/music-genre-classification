import streamlit as st
import pickle
from features import extract_features
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("🎧 Music Genre Classifier")

uploaded_file = st.file_uploader("Upload a WAV file")

if uploaded_file:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())
    
    features = extract_features("temp.wav")
    features = features.reshape(1, -1)
    
    prediction = model.predict(features)
    
    st.success(f"Predicted Genre: {prediction[0]}")