import cv2
import mediapipe as mp
import numpy as np

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


cap = cv2.VideoCapture(0)

# Canvas (drawing board)
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Previous point
prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip camera (mirror view)
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand
    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            # Draw hand points
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            # Index finger tip (landmark 8)
            index_tip = hand.landmark[8]

            h, w, _ = frame.shape
            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            # initialize previous point
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            # Draw line on canvas
            cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 255, 0), 5)

            prev_x, prev_y = x, y

    # merge canvas + camera
    output=cv2.add(frame, canvas)

    cv2.imshow("Virtual Drawing Board", output)

    key = cv2.waitKey(1) & 0xFF

    # press q to quit
    if key == ord('q'):
        break

    # press c to clear screen
    if key == ord('c'):
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)

cap.release()
cv2.destroyAllWindows()