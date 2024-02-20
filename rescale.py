import cv2 as cv

img =  cv.imread('images/cat_large.jpg')
cv.imshow('Cat', img)

def changeRes(width, height):
    #live video
    capture.set(3,width)
    capture.set(4,height)
    

def rescaleFrame(frame, scale=0.75):
    #images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
resized_img = rescaleFrame(img,scale=0.5)
cv.imshow('Image', resized_img)

capture = cv.VideoCapture('./video/dog.mp4')
cv.waitKey(0)
# while True: 
#     isTrue, frame = capture.read()
    
#     frame_resized = rescaleFrame(frame, scale=0.2)
    
#     cv.imshow('Video', frame)
#     cv.imshow("video resized", frame_resized)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
    
# capture.release()
# cv.destroyAllWindows()