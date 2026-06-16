import cv2
import mediapipe as mp
import numpy as np
import joblib
from collections import deque, Counter
import time

# Load model components
model = joblib.load("gesture_model_xgboost.pkl")
scaler = joblib.load("gesture_scaler.pkl")
label_encoder = joblib.load("gesture_label_encoder.pkl")

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Smoothing
prediction_history = deque(maxlen=10)  # Last 10 predictions
min_confidence = 0.85

# Hold detection
last_prediction = None
hold_start_time = 0
hold_threshold = 0.8  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    prediction = "No Hand"
    confident = False

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = [coord for lm in hand_landmarks.landmark for coord in (lm.x, lm.y)]
            if len(landmarks) == 42:
                input_data = np.array(landmarks).reshape(1, -1)
                input_scaled = scaler.transform(input_data)
                
                proba = model.predict_proba(input_scaled)
                max_index = np.argmax(proba)
                max_proba = proba[0][max_index]
                
                if max_proba >= min_confidence:
                    pred_label = label_encoder.inverse_transform([max_index])[0]
                    prediction_history.append(pred_label)
                    confident = True

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Smooth prediction
    if len(prediction_history) > 0:
        smoothed_prediction = Counter(prediction_history).most_common(1)[0][0]
        prediction = smoothed_prediction
    else:
        prediction = "Uncertain"

    # Hold detection
    current_time = time.time()
    if prediction == last_prediction:
        duration = current_time - hold_start_time
    else:
        hold_start_time = current_time
        duration = 0
        last_prediction = prediction

    hold_msg = f"{prediction} ({duration:.1f}s)"
    cv2.putText(frame, hold_msg, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, (0, 255, 0) if confident else (0, 0, 255), 2)

    # Optional: trigger action if gesture is held long enough
    # Example:
    # if prediction == "LeftClk" and duration > 1.0:
    #     pyautogui.click()

    cv2.imshow("Gesture Predictor", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
