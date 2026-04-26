# 🎧 Music Genre Classification

## 📌 Project Overview

This project uses **Machine Learning** to classify music into different genres such as *Rock, Jazz, Classical, Pop,* etc.
It extracts audio features from songs and predicts the genre using a trained model.

---

## 🚀 Features

* 🎵 Audio feature extraction using **MFCC (Mel Frequency Cepstral Coefficients)**
* 🤖 Machine Learning model (**Random Forest Classifier**)
* 📊 Model evaluation using accuracy score
* 🌐 Interactive web app using **Streamlit**
* 🎯 Predicts genre from uploaded audio file

---

## 🛠️ Tech Stack

* **Python**
* **Librosa** (audio processing)
* **Scikit-learn** (machine learning)
* **NumPy & Pandas**
* **Streamlit** (web app)

---

## 📂 Project Structure

```
Music-Genre-Classification/
│
├── train.py          # Model training
├── features.py       # Feature extraction (MFCC)
├── predict.py        # Genre prediction script
├── app.py            # Streamlit web app
├── model.pkl         # Saved ML model
├── .gitignore
└── README.md
```

---

## 📊 Dataset

* GTZAN Music Genre Dataset
* Contains 10 genres:

  * Blues, Classical, Country, Disco, HipHop
  * Jazz, Metal, Pop, Reggae, Rock

⚠️ Dataset is not included in this repository due to size.
Download from: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/music-genre-classification.git
cd music-genre-classification
```

### 2. Install dependencies

```
pip install numpy pandas matplotlib librosa scikit-learn streamlit
```

### 3. Run training

```
python train.py
```

### 4. Run prediction

```
python predict.py
```

### 5. Run web app

```
python -m streamlit run app.py
```

---

## 🎯 Model Performance

* Algorithm: Random Forest
* Accuracy: ~60–65% (basic implementation)

---

## 💡 Future Improvements

* Use **CNN with spectrograms** for higher accuracy
* Add more audio features (Chroma, Spectral Contrast)
* Deploy as a web application
* Real-time audio classification

---

## 📸 Demo

Upload a `.wav` file in the Streamlit app to get genre prediction.

---

## 👨‍💻 Author

* Divya Chauhan

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
