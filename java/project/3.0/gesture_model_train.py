import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder, StandardScaler
import xgboost as xgb
import joblib

# Load the dataset
df = pd.read_csv("gesture_data.csv", header=None)

# The last column contains the labels
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Remove unwanted gestures
unwanted_labels = ['ScreenShort', 'Exit']
mask = ~y.isin(unwanted_labels)
X = X[mask]
y = y[mask]

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Train XGBoost classifier
model = xgb.XGBClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save the model and tools
joblib.dump(model, 'gesture_xgb_model.pkl')
joblib.dump(scaler, 'gesture_scaler.pkl')
joblib.dump(le, 'gesture_label_encoder.pkl')
print("✅ Model and preprocessing tools saved.")
