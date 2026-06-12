import cv2 as c
import numpy as np

img = c.imread("image2.png")

g=img[:,:,1]
r=img[:,:,2]
b=img[:,:,0]

z=np.zeros_like(img)

z[:,:,0]=b
z[:,:,2]=r

c.imshow("image",z)
c.waitKey(0)
c.destroyAllWindows()