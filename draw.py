import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('blank',blank)
img = cv.imread('images/cat.jpg')
#cv.imshow('pussy',img)

# 1. paint 

blank[200:300 , 300:400]= 0,0,255
cv.imshow('Green', blank)

cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=cv.FILLED)
cv.imshow("rectangle",blank)
cv.waitKey(0)
