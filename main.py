import cv2
import mediapipe as mp
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mphands = mp.solutions.hands

cap = cv2.VideoCapture(0)
hands = mphands.Hands()

prev_thumb_y = 0
prev_index_finger_y = 0
prev_index_finger_x = 0

alpha = 0.5

while True:
    data, image = cap.read()

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks, mphands.HAND_CONNECTIONS)

            thumb_y = hand_landmarks.landmark[4].y
            thumb_x = hand_landmarks.landmark[4].x

            index_finger_y = hand_landmarks.landmark[8].y * 2500
            index_finger_x = hand_landmarks.landmark[8].x * 3900

            middle_finger_y = hand_landmarks.landmark[12].y
            middle_finger_x = hand_landmarks.landmark[12].x

            ring_finger_y = hand_landmarks.landmark[16].y
            ring_finger_x = hand_landmarks.landmark[16].x

            pinky_finger_y = hand_landmarks.landmark[20].y
            pinky_finger_x = hand_landmarks.landmark[20].x

            index_finger_x = alpha * index_finger_x + (1 - alpha) * prev_index_finger_x
            index_finger_y = alpha * index_finger_y + (1 - alpha) * prev_index_finger_y

            pyautogui.moveTo(index_finger_x, index_finger_y)

            prev_index_finger_x, prev_index_finger_y = index_finger_x, index_finger_y

            tolerance = 0.02

    cv2.waitKey(10)
