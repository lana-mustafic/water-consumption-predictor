# 💧 Water Consumption Predictor

A simple machine learning project that predicts daily water consumption based on household data.  
It uses a trained `RandomForestRegressor` model in the backend (Flask API) and a Tkinter-based GUI as the frontend.  

This project was built as part of an initiative to combine **data science** with **user-friendly desktop apps** — making machine learning more accessible to everyday users.

---

## 🧠 Features

- Predicts daily water consumption based on:
  - Number of household occupants
  - Average temperature
  - Household type (Apartment/House)
  - Outdoor activities (Yes/No)
- Machine learning backend (Python, scikit-learn, Flask)
- Desktop GUI built with Tkinter
- CORS support for API interaction
- Model serialization with Joblib
- Preprocessing using `ColumnTransformer` + `OneHotEncoder`

---

## 🗂️ Project Structure

water-consumption-predictor/
├── backend/
│ ├── app.py # Flask API for prediction
│ ├── models/
│ │ ├── water_model.joblib # Trained ML model
│ │ └── preprocessor.joblib # Saved preprocessor
│ └── data_water_consumption.xlsx # Dataset
│
├── frontend/
│ └── gui_app.py # Tkinter GUI app
│
├── requirements.txt
└── README.md # You are here


---

## 🧪 Dataset

The dataset contains the following columns:

| Column                  | Type   | Description                                 |
|-------------------------|--------|---------------------------------------------|
| Number_of_Occupants     | int    | People living in the household              |
| Average_Temperature     | float  | Daily average temperature in Celsius        |
| Household_Type          | string | Apartment or House                          |
| Outdoor_Activities      | string | 'Yes' or 'No'                               |
| Daily_Water_Consumption | float  | Target value in liters                      |

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/water-consumption-predictor.git
   cd water-consumption-predictor
