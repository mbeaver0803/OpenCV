import glob
import cv2
import os
import sys
import shutil
import piexif
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter

imagePath = input("Enter the path of your images: ")
while os.path.exists(imagePath) is False:
    print('Path was not found please try again')
    imagePath = input("Enter the path of your images: ")

print('Path was found.')

rgbPathS = imagePath + r'Sharpened'
if not os.path.exists(rgbPathS):
    os.makedirs(rgbPathS)

#nrgPathS = imagePath + r'\SharpenedNRG'
#if not os.path.exists(nrgPathS):
#    os.makedirs(nrgPathS)


#errorCounter1 = 0
#errorCounter2 = 0

for filename in os.listdir(imagePath):
    if  filename.endswith('.JPG'): #filename.startswith('RGB') and
        imageName = os.path.splitext(filename)[0]
        print(imageName)
        img0 = cv2.imread(filename)
        # converting to gray scale
        # gray = cv2.cvtColor(img0, cv2.COLOR_RGB2GRAY)

        # remove noise
        img = cv2.GaussianBlur(img0,(3,3),0)

        #sharpen image
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        img = cv2.filter2D(img, -1, kernel)
        #backtorgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        #cv2.imshow('Sharpend Image', backtorgb)
        #cv2.waitKey(0)
        cv2.imwrite( imageName+'_Sharpened.JPG', img )

            #try:
            #piexif.transplant(filename, imageName+'_Sharpened.JPG')
            #except:
            #print(imageName +' has no EXIF data.')
            #errorCounter1 += 1
 
        shutil.move(imageName+'_Sharpened.JPG', rgbPathS)



for filename in os.listdir(imagePath):
    if filename.startswith('NRG') and filename.endswith('.JPG'):
        imageName = os.path.splitext(filename)[0]
        print(imageName)
        img0 = cv2.imread(filename)
        # converting to gray scale
        # gray = cv2.cvtColor(img0, cv2.COLOR_RGB2GRAY)

        # remove noise
        img = cv2.GaussianBlur(img0,(3,3),0)

        #sharpen image
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        img = cv2.filter2D(img, -1, kernel)
        #backtorgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        #cv2.imshow('Sharpend Image', backtorgb)
        #cv2.waitKey(0)
        cv2.imwrite( imageName +'_Sharpened.JPG', img )

        try:
            piexif.transplant(filename, imageName+'_Sharpened.JPG')
        except:
            print(imageName +' has no EXIF data.')
            errorCounter2 += 1

        shutil.move(imageName +'_Sharpened.JPG', nrgPathS)


    
