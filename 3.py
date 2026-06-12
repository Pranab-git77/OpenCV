import cv2 as c

# STEP 1: IMAGE INPUT
img = c.imread("image.png")


if img is None:
    print("Image not found!")
else:

    sharpended=c.medianBlur(img, 5)

    height, width = img.shape[:2]
    print(f"Image Dimensions: {width}x{height}")
    print(f"total pixels: {width*height}")

    c.imshow("Original Image", img)
    c.imshow("Sharpended Image", sharpended)

    c.waitKey(0)
    c.destroyAllWindows()