import cv2 as c
import mediapipe as m
import numpy as n

cam=c.VideoCapture(0)

m_hand=m.solutions.hands
hands=m_hand.Hands(min_detection_confidence=0.4,min_tracking_confidence=0.4)
m_drawing=m.solutions.drawing_utils

prev_xindex,prev_yindex=0,0
emp_can=None

while True:
    ret,frame=cam.read()
    if not ret:
        break
    frame = c.flip(frame, 1)
    framec=c.cvtColor(frame,c.COLOR_BGR2RGB)
    h,w=frame.shape[:2]
    hand=hands.process(framec)

    if hand.multi_hand_landmarks:
        for poi in hand.multi_hand_landmarks:
            index=poi.landmark

            cindex_x,cindex_y=int(index[8].x*w),int(index[8].y*h)

            if not(prev_xindex and prev_yindex):
                prev_xindex,prev_yindex=cindex_x,cindex_y

            if emp_can is None:
                emp_can=n.zeros_like(frame)

            c.line(emp_can,(prev_xindex,prev_yindex),(cindex_x,cindex_y),(255,0,255),6)
            

            m_drawing.draw_landmarks(frame, poi, m_hand.HAND_CONNECTIONS)

            prev_xindex,prev_yindex=cindex_x,cindex_y
    
    else:
        prev_xindex,prev_yindex=0,0
    if emp_can is not None:
        frame=c.add(frame,emp_can)
    c.imshow("LED Control", frame)

    if c.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
c.destroyAllWindows()