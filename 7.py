import cv2 as c
import mediapipe as m
import math

mp_hands = m.solutions.hands
hands = mp_hands.Hands()
mp_draw = m.solutions.drawing_utils

cap = c.VideoCapture(0)

led_on = False
prev_pinch = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = c.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = c.cvtColor(frame, c.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lm = handLms.landmark

            x1, y1 = int(lm[4].x * w), int(lm[4].y * h)   # thumb tip
            x2, y2 = int(lm[8].x * w), int(lm[8].y * h)   # index tip

            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            # pinch detection
            pinch = distance < 40
            print(f"Distance: {distance}, Pinch: {pinch}")

            if pinch and not prev_pinch:
                led_on = not led_on

            prev_pinch = pinch

            if led_on:
                color = (0, 255, 0) if led_on else (0, 0, 255)
            else:
                color = (0, 0, 255)
            c.circle(frame, (100, 100), 30, color, -1)

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    c.imshow("LED Control", frame)

    if c.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
c.destroyAllWindows()