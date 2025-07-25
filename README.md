# 💧 Water Consumption Predictor

A machine learning system that predicts household water consumption with **85% accuracy**. Combines a Flask API backend with an intuitive Tkinter GUI.

## 🚀 Features

### Predictive Analytics
- 📊 Forecasts daily water usage (in liters)
- 🌡️ Accounts for weather and household characteristics
- 🔄 Automatic retraining when new data is added

### Technical Stack
| Component          | Technology |
|--------------------|------------|
| Machine Learning   | scikit-learn |
| Backend API        | Flask      |
| Frontend           | Tkinter    |

## 📂 Project Structure

```bash
water-consumption-predictor/
├── backend/
│   ├── app.py              # Flask API
│   ├── models/             # ML artifacts
│   └── data_water_consumption.xlsx
├── frontend/
│   └── gui_app.py          # Tkinter GUI
└── requirements.txt

```

##🛠️ Installation
```

git clone https://github.com/lana-mustafic/water-consumption-predictor.git
cd water-consumption-predictor
pip install -r requirements.txt

```

###🏃‍♂️ Quick Start
Launch Backend:

```

cd backend
python app.py
Run GUI:

```
cd ../frontend
python gui_app.py

```
###🤝 How to Contribute
Fork the repository

Create feature branches

Submit PRs with tests

##📜 License
MIT © 2023 Lana Mustafić