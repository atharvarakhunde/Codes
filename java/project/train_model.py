import cv2
import mediapipe as mp
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Feature extraction function
def extract_features(hand_landmarks):
    features = []
    for landmark in hand_landmarks.landmark:
        features.extend([landmark.x, landmark.y])
    return features

# Define gesture labels
GESTURE_LABELS = {
    0: "Move",
    1: "NoMove",
    2: "RightClick",
    3: "LeftClick"
}

# Collect training data
features_list = []
labels_list = []

for label, gesture in GESTURE_LABELS.items():
    print(f"Collecting data for: {gesture}")
    cap = cv2.VideoCapture(0)
    collected = 0
    while collected < 800:
        ret, frame = cap.read()
        if not ret:
            break
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0]
            features = extract_features(landmarks)
            if len(features) == 42:
                features_list.append(features)
                labels_list.append(label)
                collected += 1
                print(f"{gesture}: {collected}/100")
        cv2.imshow("Collecting Gesture", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

# Convert to numpy arrays
X = np.array(features_list)
y = np.array(labels_list)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = RandomForestClassifier()
model.fit(X_scaled, y)

# Save model and scaler
joblib.dump(model, 'gesture_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Training complete.")
