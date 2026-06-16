import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix

# Load the trained model and preprocessing tools
model = joblib.load('gesture_xgb_model.pkl')
scaler = joblib.load('gesture_scaler.pkl')
le = joblib.load('gesture_label_encoder.pkl')

# Load test data
df = pd.read_csv("gesture_data_test.csv")  # Make sure it includes a 'label' column if you want evaluation

# Check if 'label' column is present
has_labels = 'label' in df.columns

# Separate features and labels (if available)
if has_labels:
    X = df.drop("label", axis=1)
    y = df["label"]
else:
    X = df
    y = None

# Scale features
X_scaled = scaler.transform(X)

# Predict
y_pred = model.predict(X_scaled)
predicted_labels = le.inverse_transform(y_pred)

# Print predictions
print("\n🧠 Predictions:")
for i, label in enumerate(predicted_labels):
    print(f"Sample {i+1}: Predicted Gesture → {label}")

# Evaluate performance if true labels exist
if has_labels:
    y_true_encoded = le.transform(y)
    print("\n📊 Classification Report:")
    print(classification_report(y_true_encoded, y_pred, target_names=le.classes_))
    
    print("🧮 Confusion Matrix:")
    print(confusion_matrix(y_true_encoded, y_pred))
