import joblib
import numpy as np

class calorieBurn:
    def __init__(self):
        self.model = joblib.load('calorie_model.pkl')
        self.scaler = joblib.load('scaler.pkl')

    def predict(self, gender, age, duration, heart_beat, temp, bmi):
        input_data = np.array([[gender, age, duration, heart_beat, temp, bmi]])
        
        # Scale the input data using the same scaler
        input_scaled = self.scaler.transform(input_data)

        # Predict using the scaled data
        result = self.model.predict(input_scaled)

        return np.clip(result, 0, None)  # Ensure no negative predictions
