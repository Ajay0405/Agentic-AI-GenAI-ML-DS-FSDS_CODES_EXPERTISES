import cv2
src = cv2.imread(r'logo.png')  # Read the image

# Convert to Grayscale
# Display
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()