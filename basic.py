import cv2 as cv

img = cv.imread('./images/park.jpg')
cv.imshow('park',img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# eroded = cv.erode(dilated, kernel=(7,7), iterations=3)
# cv.imshow("eroded",eroded)

# Resize

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)
cv.waitKey(0)