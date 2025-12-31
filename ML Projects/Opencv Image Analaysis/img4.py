import cv2

src = cv2.imread("image.jpg")

if src is None:
    print("Error: Image not loaded")
else:
    converted = cv2.cvtColor(src, cv2.COLOR_Luv2BGR)
