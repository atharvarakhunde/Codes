import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pyautogui
import pickle
import time

# Load the trained model
model = load_model("gesture_model.h5")
print("Model loaded successfully.")

# Load the label encoder
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)
print("Label encoder loaded.")

# Load dataset for consistent scaling
data = pd.read_csv("gesture_data.csv")
X = data.iloc[:, :-1].values  # only features
scaler = StandardScaler()
scaler.fit(X)

# Simulated real-time loop (replace this with camera input or live data later)
print("Starting gesture control loop. Press Ctrl+C to stop.")
try:
    while True:
        # --- Replace this with real input from camera/sensor ---
        # Simulate gesture input by using a known sample from the dataset
        sample_input_array = X[0].reshape(1, -1)  # simulate live input

        # Scale the input
        sample_scaled = scaler.transform(sample_input_array)

        # Predict gesture
        prediction = model.predict(sample_scaled)
        predicted_class_index = np.argmax(prediction)
        predicted_class_label = label_encoder.inverse_transform([predicted_class_index])[0]

        print("Gesture:", predicted_class_label)

        # --- Perform action based on prediction ---
        if predicted_class_label == "move":
            pyautogui.moveRel(20, 0)  # move mouse 20px right
        elif predicted_class_label == "left_click":
            pyautogui.click(button='left')
        elif predicted_class_label == "right_click":
            pyautogui.click(button='right')
        elif predicted_class_label == "none":
            pass  # do nothing

        time.sleep(1)  # control the speed of gesture polling

except KeyboardInterrupt:
    print("Gesture control stopped.")
