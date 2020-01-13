import cv2
import numpy as np
from matplotlib import pyplot as plt

original_image = cv2.imread("Test1.png")
hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

roi = cv2.imread("Test1_1.png")
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_roi)

#Histogram ROI
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
mask = cv2.calcBackProject([hsv_original], [0, 1], roi_hist, [0, 180, 0, 256], 1)

#kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

#Filter out noise
mask = cv2.filter2D(mask, -1, kernel)
_, mask = cv2.threshold(mask, 30, 255, cv2.THRESH_BINARY)

cv2.imshow("Mask", mask)
cv2.imshow("Original Image", original_image)
cv2.imshow("Roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.imshow(roi_hist)
#plt.show()
