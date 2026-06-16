import cv2
import mediapipe as mp
import pyautogui
import math

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

def get_finger_status(lmList):
    tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky tips
    fingers = []
    
    # Thumb
    if lmList[4][0] < lmList[3][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other four fingers
    for tip in tips:
        if lmList[tip][1] < lmList[tip - 2][1]:
            fingers.append(1)
        else:
            fingers.append(0)
    
    return fingers  # Returns list like [0,1,1,1,0]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            if lmList:
                fingers = get_finger_status(lmList)

                # Move cursor: Only index finger up
                if fingers == [0, 1, 0, 0, 0]:
                    x, y = lmList[8]  # Index fingertip
                    screen_x = screen_width * x / w
                    screen_y = screen_height * y / h
                    pyautogui.moveTo(screen_x, screen_y)

                # Stop cursor: All 5 fingers up
                elif fingers == [1, 1, 1, 1, 1]:
                    pass  # Do nothing (stop cursor movement)

                # Copy: 3 fingers (index + middle + ring)
                elif fingers == [0, 1, 1, 1, 0]:
                    pyautogui.hotkey('ctrl', 'c')
                    pyautogui.sleep(0.4)

                # Paste: 4 fingers up (no thumb)
                elif fingers == [0, 1, 1, 1, 1]:
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.sleep(0.4)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("AI Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
