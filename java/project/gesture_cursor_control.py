import cv2
import mediapipe as mp
import pyautogui
import joblib
import time
from pynput.mouse import Button, Controller

# Load trained model and scaler
model = joblib.load("gesture_model.pkl")
scaler = joblib.load("scaler.pkl")

# Initialize
mouse = Controller()
screen_width, screen_height = pyautogui.size()

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Gesture labels
GESTURE_LABELS = {
    0: "Move",
    1: "NoMove",
    2: "RightClick",
    3: "LeftClick"
}

# Feature extraction
def extract_features(hand_landmarks):
    return [coord for lm in hand_landmarks.landmark for coord in (lm.x, lm.y)]

# Video capture setup
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Cursor smoothing and click delay
prev_x, prev_y = 0, 0
smoothening = 7
last_click_time = time.time()
click_delay = 1

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                features = extract_features(hand_landmarks)

                if len(features) == 42:
                    features_scaled = scaler.transform([features])
                    prediction = model.predict(features_scaled)[0]
                    gesture = GESTURE_LABELS.get(prediction, "Unknown")

                    cv2.putText(frame, f"Gesture: {gesture}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                                1.5, (0, 255, 0), 3, cv2.LINE_AA)

                    # Mouse control
                    index_tip = hand_landmarks.landmark[8]
                    cursor_x = index_tip.x * screen_width
                    cursor_y = index_tip.y * screen_height

                    if gesture == "Move":
                        smoothed_x = prev_x + (cursor_x - prev_x) / smoothening
                        smoothed_y = prev_y + (cursor_y - prev_y) / smoothening
                        pyautogui.moveTo(smoothed_x, smoothed_y)
                        prev_x, prev_y = smoothed_x, smoothed_y
                    elif gesture == "LeftClick" and time.time() - last_click_time > click_delay:
                        mouse.press(Button.left)
                        mouse.release(Button.left)
                        last_click_time = time.time()
                    elif gesture == "RightClick" and time.time() - last_click_time > click_delay:
                        mouse.press(Button.right)
                        mouse.release(Button.right)
                        last_click_time = time.time()

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
