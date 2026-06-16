import joblib

# Load your original model
model = joblib.load('gesture_model.pkl')

# Save it again with a compatible protocol
joblib.dump(model, 'gesture_model_compatible.pkl', protocol=3)

print("Model saved as 'gesture_model_compatible.pkl'")
