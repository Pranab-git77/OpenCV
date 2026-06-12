import cv2 as c

cap = c.VideoCapture(0)

blur_val = 3

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = c.cvtColor(frame, c.COLOR_BGR2GRAY)

    key = c.waitKey(1) & 0xFF

    if key == ord('w'):
        blur_val += 2
    elif key == ord('s'):
        blur_val -= 2


    if blur_val < 3:
        blur_val = 3
    if blur_val % 2 == 0:
        blur_val += 1

    blurred = c.GaussianBlur(gray, (blur_val, blur_val), 0)
    edges = c.Canny(blurred, 50, 150)

    c.imshow("Edges", edges)

    if key == ord('q'):
        break

cap.release()
c.destroyAllWindows()