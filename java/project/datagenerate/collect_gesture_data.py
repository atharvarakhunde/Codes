import cv2
import mediapipe as mp
import pandas as pd
import time
import os

# Setup MediaPipe and drawing
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Open camera
cap = cv2.VideoCapture(0)

# Get multiple gestures from user
gesture_labels = input("Enter gesture labels separated by comma (e.g., move,click,copy): ").split(',')
gesture_labels = [label.strip() for label in gesture_labels]

samples = []
sample_limit = 100  # per gesture

columns = [f'x{i}' for i in range(21)] + [f'y{i}' for i in range(21)] + ['label']

for gesture_label in gesture_labels:
    print(f"\n🖐️ Show gesture '{gesture_label}' to the camera...")
    time.sleep(3)  # Give user time to prepare

    count = 0
    while count < sample_limit:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                landmark_list = []
                for lm in hand_landmarks.landmark:
                    landmark_list.extend([lm.x, lm.y])

                samples.append(landmark_list + [gesture_label])
                count += 1

                # Draw landmarks
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Show collection progress
        cv2.putText(frame, f"Collecting {gesture_label}: {count}/{sample_limit}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow("Gesture Data Collector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print("\n✅ Collection complete.")

# Release and destroy
cap.release()
cv2.destroyAllWindows()

# Save to CSV
df = pd.DataFrame(samples, columns=columns)
file_exists = os.path.exists("gesture_data_test.csv")
df.to_csv("gesture_data_test.csv", mode='a', index=False, header=not file_exists)

print(f"✅ Saved all samples to 'gesture_data.csv'. Total gestures: {gesture_labels}")
