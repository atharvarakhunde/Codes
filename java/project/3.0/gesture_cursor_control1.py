import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import pickle
from tensorflow.keras.models import load_model

# Load model and label encoder
model = load_model("gesture_model.h5")
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Screen dimensions
screen_width, screen_height = pyautogui.size()

# Webcam
cap = cv2.VideoCapture(0)

print("🖐️ Gesture control started... Press 'Q' to quit")

last_action = None
cooldown_frames = 20
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y])

            if len(landmarks) == 42:
                input_data = np.array(landmarks).reshape(1, -1)
                prediction = model.predict(input_data)
                predicted_label = label_encoder.classes_[np.argmax(prediction)]

                cv2.putText(frame, f"Gesture: {predicted_label}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

                index_finger = hand_landmarks.landmark[8]
                x = int(index_finger.x * screen_width)
                y = int(index_finger.y * screen_height)

                if predicted_label != last_action or frame_count > cooldown_frames:
                    if predicted_label == 'Move':
                        pyautogui.moveTo(x, y)
                    elif predicted_label == 'RightClk':
                        pyautogui.click(button='right')
                    elif predicted_label == 'LeftClk':
                        pyautogui.click(button='left')

                    last_action = predicted_label
                    frame_count = 0
                else:
                    frame_count += 1

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Cursor Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Gesture control ended.")
