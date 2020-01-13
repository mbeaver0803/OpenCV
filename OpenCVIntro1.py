import numpy as np
import cv2
from matplotlib import pyplot as plt

#read an image
#img = cv2.imread('Telluride.jpg', 0)
#display an image
#cv2.imshow('Image', img)
#key to end program ."0" for this program
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#write an image
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('NewImage', img)
#cv2.waitKey(0)
#cv2.destroyallWindows()

#using Matplotlib
img = cv2.imread('Telluride.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
