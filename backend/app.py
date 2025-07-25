from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# Define preprocessing
numeric_features = ['Number_of_Occupants', 'Average_Temperature']
categorical_features = ['Household_Type', 'Outdoor_Activities']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Create and train model pipeline
def train_model():
    
    data = {
        'Number_of_Occupants': [1, 2, 3, 4, 5, 6, 7, 2, 3, 4],
        'Average_Temperature': [15, 20, 18, 22, 25, 19, 21, 20, 23, 17],
        'Household_Type': ['Apartment', 'House', 'Apartment', 'House', 'Apartment', 
                          'House', 'Apartment', 'Apartment', 'House', 'House'],
        'Outdoor_Activities': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No'],
        'Daily_Water_Consumption': [120, 200, 150, 220, 250, 180, 210, 170, 200, 190]
    }
    df = pd.DataFrame(data)
    
    X = df.drop('Daily_Water_Consumption', axis=1)
    y = df['Daily_Water_Consumption']
    
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))
    ])
    
    model.fit(X, y)
    
    # Save model and preprocessor
    joblib.dump(model.named_steps['regressor'], 'models/water_model.joblib')
    joblib.dump(preprocessor, 'models/preprocessor.joblib')
    
    return model

# Load model and preprocessor
try:
    model = joblib.load('models/water_model.joblib')
    preprocessor = joblib.load('models/preprocessor.joblib')
except:
    print("Training model for the first time...")
    model = train_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Convert to DataFrame
        input_data = pd.DataFrame([data])
        
        # Preprocess the data
        processed_data = preprocessor.transform(input_data)
        
        # Make prediction
        prediction = model.predict(processed_data)
        
        return jsonify({
            'prediction': round(float(prediction[0]), 2),
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)