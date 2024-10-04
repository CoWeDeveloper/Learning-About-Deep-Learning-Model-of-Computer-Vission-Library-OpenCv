import cv2 as cv 


img = cv.imread('Photos/cat.jpg') #cv.imread() this function read the image.
cv.imshow('blackCat', img) #cv.imshow() this function show the read image in a new window, which name we have given.

cv.waitKey(0) # the window box time it will show. 0 mean infinite (until we close it)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleContent(frame)

    cv.imshow("cuteDog", frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()