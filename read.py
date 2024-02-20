import cv2 as cv

#img = cv.imread('images/cat_large.jpg')

#cv.imshow('cutie', img)

#

capture = cv.VideoCapture('./video/How Green Roofs Can Help Cities  NPR.mp4')

while True: 
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.waitKey(0)
