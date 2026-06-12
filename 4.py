import cv2 as c
import numpy as n

cam=c.VideoCapture(0)
a=0

def grid(fra):
    if a==1:
        height,width=fra.shape[:2]
        do_fra=c.resize(fra,(width//2,height//2))
        tl_fra=do_fra
        tr_fra=c.flip(tl_fra,0)
        bl_fra=c.cvtColor(tl_fra,c.COLOR_BGR2HSV)
        red=do_fra[:,:,2]
        br_fra = n.zeros_like(do_fra)
        br_fra[:, :, 2] = red
        top_row = n.hstack((tl_fra, tr_fra))
        bottom_row = n.hstack((bl_fra, br_fra))
        grid_window = n.vstack((top_row, bottom_row))
        c.imshow("Grid", grid_window)

while True:
    to,fra=cam.read()

    if not to:
        break

    fli_fra=c.flip(fra,1)

    c.imshow("Webcam",fli_fra)
    k=c.waitKey(1) & 0xFF
    grid(fli_fra)
    if k==ord('c') and a!=1:
        a+=1
    if k==ord('s'):
        height,width=fra.shape[:2]
        fli_fra=c.resize(fli_fra,(width//2,height//2))
        fli_fra=c.cvtColor(fli_fra,c.COLOR_BGR2GRAY)
        c.imshow(f"Resized Webcam{a}",fli_fra)
        

    elif k==ord('q'):
        break


cam.release()
c.destroyAllWindows()

