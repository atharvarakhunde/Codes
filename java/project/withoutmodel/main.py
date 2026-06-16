import cv2
import mediapipe as mp
import pyautogui
import random
import util
import numpy as np
from collections import deque
from pynput.mouse import Button, Controller
import time

mouse = Controller()
screen_width, screen_height = pyautogui.size()

# Mediapipe Hands setup
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

# Movement smoothing
position_buffer = deque(maxlen=5)

def smooth_position(x, y):
    position_buffer.append((x, y))
    avg_x = sum(p[0] for p in position_buffer) / len(position_buffer)
    avg_y = sum(p[1] for p in position_buffer) / len(position_buffer)
    return int(avg_x), int(avg_y)

# Gesture hold logic
gesture_frame_count = {"left": 0, "right": 0, "double": 0, "screenshot": 0}
GESTURE_THRESHOLD = 5

# Gesture definitions
def is_left_click(landmark_list, dist):
    return util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and \
           util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) > 90 and dist > 50

def is_right_click(landmark_list, dist):
    return util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and \
           util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90 and dist > 50

def is_double_click(landmark_list, dist):
    return util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and \
           util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and dist > 50

def is_screenshot(landmark_list, dist):
    return util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and \
           util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and dist < 50

# Cursor control
def move_mouse(index_finger_tip):
    x, y = smooth_position(index_finger_tip.x * screen_width, index_finger_tip.y * screen_height)
    pyautogui.moveTo(x, y)

# Gesture detection
def detect_gesture(frame, landmark_list, processed):
    if len(landmark_list) < 21:
        return

    index_finger_tip = processed.multi_hand_landmarks[0].landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
    thumb_index_dist = util.get_distance([landmark_list[4], landmark_list[5]])

    if thumb_index_dist < 50 and util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90:
        move_mouse(index_finger_tip)
    elif is_left_click(landmark_list, thumb_index_dist):
        gesture_frame_count["left"] += 1
        if gesture_frame_count["left"] >= GESTURE_THRESHOLD:
            mouse.click(Button.left)
            cv2.putText(frame, "Left Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            gesture_frame_count["left"] = 0
    elif is_right_click(landmark_list, thumb_index_dist):
        gesture_frame_count["right"] += 1
        if gesture_frame_count["right"] >= GESTURE_THRESHOLD:
            mouse.click(Button.right)
            cv2.putText(frame, "Right Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            gesture_frame_count["right"] = 0
    elif is_double_click(landmark_list, thumb_index_dist):
        gesture_frame_count["double"] += 1
        if gesture_frame_count["double"] >= GESTURE_THRESHOLD:
            pyautogui.doubleClick()
            cv2.putText(frame, "Double Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            gesture_frame_count["double"] = 0
    elif is_screenshot(landmark_list, thumb_index_dist):
        gesture_frame_count["screenshot"] += 1
        if gesture_frame_count["screenshot"] >= GESTURE_THRESHOLD:
            im = pyautogui.screenshot()
            label = random.randint(1, 1000)
            im.save(f'my_screenshot_{label}.png')
            cv2.putText(frame, "Screenshot Taken", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            gesture_frame_count["screenshot"] = 0
    else:
        for key in gesture_frame_count:
            gesture_frame_count[key] = 0

# Main loop
def main():
    draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frameRGB)

            landmark_list = []
            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
                for lm in hand_landmarks.landmark:
                    landmark_list.append((lm.x, lm.y))

            detect_gesture(frame, landmark_list, processed)

            cv2.imshow('Hand Gesture Control', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
