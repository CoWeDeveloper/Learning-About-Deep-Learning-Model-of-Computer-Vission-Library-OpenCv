import cv2 as cv 

img = cv.imread('Photos/cat.jpg') #cv.imread() this function read the image.
cv.imshow('blackCat', img) #cv.imshow() this function show the read image in a new window, which name we have given.

cv.waitKey(0) # the window box time it will show. 0 mean infinite (until we close it)

# This function helps to change the size of image
def rescaleContent(frame, scale =0.75):
    width = int(frame.shape[1] * scale) # frame.shape[1] targe the width of the frame 
    height = int(frame.shape[0] * scale)# frame.shape[0] targe the height of the frame

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resize_image = rescaleContent(img)
cv.imshow("image_size_change", resize_image)
cv.waitKey(0)






# -----------------working with the video-------------------------
capture = cv.VideoCapture('Videos/dog.mp4')

# this function/method will work only on live video. now work on existing video. 
# for that you have to use rescaleContent. 
def changeRef(width, height):
    capture.set(3, width)
    capture.set(4, height)

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleContent(frame)

#     cv.imshow("cuteDog", frame)
#     cv.imshow('Video Resized', frame_resized)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()