import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import joblib
import time
import traceback
from datetime import datetime

# Load trained models
print("Loading model files...")
model = joblib.load('gesture_xgb_model.pkl')
scaler = joblib.load('gesture_scaler.pkl')
le = joblib.load('gesture_label_encoder.pkl')
print("Models loaded successfully.")

# Disable PyAutoGUI fail-safe (use with caution)
pyautogui.FAILSAFE = False

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()
print(f"Screen resolution: {screen_w}x{screen_h}")

# DPI multiplier for faster movement
DPI_MULTIPLIER = 1.5

# Gesture to action map
def perform_action(gesture, x, y):
    if gesture == "Move":
        pyautogui.moveTo(x * DPI_MULTIPLIER, y * DPI_MULTIPLIER)
    elif gesture == "LeftClk":
        pyautogui.click()
        time.sleep(0.2)
    elif gesture == "RightClk":
        pyautogui.rightClick()
        time.sleep(0.2)
    # "NotMove" → do nothing

# Main loop
cap = cv2.VideoCapture(0)
print("Starting video capture. Press ESC to quit.")
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmark_list = []
                for lm in hand_landmarks.landmark:
                    landmark_list.extend([lm.x, lm.y])

                if len(landmark_list) == 42:  # Only use x and y for 21 points
                    landmarks_scaled = scaler.transform([landmark_list])
                    prediction = model.predict(landmarks_scaled)
                    gesture = le.inverse_transform(prediction)[0]

                    # Cursor location using index finger tip (landmark 8)
                    index_finger = hand_landmarks.landmark[8]
                    cursor_x = int(index_finger.x * screen_w)
                    cursor_y = int(index_finger.y * screen_h)

                    perform_action(gesture, cursor_x, cursor_y)

                    cv2.putText(frame, f'Gesture: {gesture}', (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

except Exception as e:
    log_file = f"error_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(log_file, 'w') as f:
        f.write("Exception in gesture control script:\n")
        f.write(traceback.format_exc())
    print(f"Exception occurred, saved log to {log_file}")

finally:
    cap.release()
    cv2.destroyAllWindows()
