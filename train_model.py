import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

# Load data
data = pd.read_csv('dataframe.csv')
X = data[['Gender', 'Age', 'Duration', 'Heart_Rate', 'Body_Temp', 'BMI']]
y = data['Calories']

# Standardise data
Scaler = StandardScaler()
X_scalar = Scaler.fit_transform(X)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X_scalar, y, test_size=0.2, random_state=42)
knn = KNeighborsRegressor(n_neighbors=13)
knn.fit(X_train, y_train)

#Save Model
joblib.dump(knn, 'calorie_model.pkl')
joblib.dump(Scaler, 'scaler.pkl')
