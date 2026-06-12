import cv2 as c
import time as t

cap = c.VideoCapture(0)

time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = t.time()
    fps = 1 / (current_time - time)
    time = current_time


    c.putText(frame, f"FPS: {int(fps)}", (20, 40),c.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    c.imshow("Webcam Feed", frame)

    key = c.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"frame_{int(t.time())}.jpg"
        c.imwrite(filename, frame)
        print("Saved:", filename)

    elif key == ord('q'):
        break

cap.release()
c.destroyAllWindows()