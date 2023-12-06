'''first step is capturing a blank wall and saving the image in the variable firstframe
when we bring in the object we have the subtract the object frame and the wall frame
by doing this we can get thee object position which enables us the get the object area and draw rectangle'''

import cv2  #for image
import time #for time delay
import imutils  #for resize

cam = cv2.VideoCapture(0)  #camera port
time.sleep(1)  #1 sec time delay

firstframe = None
area = 500 #default threshold value

while True: #continous loop so that it looks like a video
    a, img = cam.read() #read frame from the camera
    text = "normal"
    img = imutils.resize(img, width=500) #resize due to change in resolution of cameras
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color to grayscale image
    gaussian = cv2.GaussianBlur(grayimg, (21,21), 0) #smoothening this helps to aplly thresold easy
    if firstframe is None:
        firstframe = gaussian   #capturinng first frame on iteration
        continue
    imgdiff = cv2.absdiff(firstframe, gaussian)
    threshimg = cv2.threshold(imgdiff, 25,255,cv2.THRESH_BINARY)[1]
    threshimg = cv2.dilate(threshimg, None, iterations=2) #to threshold completely
    cnts = cv2.findContours(threshimg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) <area:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
        text = "moving object detected"
        print(text)
        cv2.putText(img, text, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()  # to relaese the camera to prevent the use of camera after ending the function
cv2.destroyAllWindows()







