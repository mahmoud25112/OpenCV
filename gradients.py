import cv2 as cv
import numpy as np

img = cv.imread('images/park.jpg')
cv.imshow('park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelx,sobely)
cv.imshow("combined", combined)
cv.imshow('Laplacian', lap)
cv.waitKey(0)
