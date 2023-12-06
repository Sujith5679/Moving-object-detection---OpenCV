# Moving-object-detection---OpenCV
this is just a simple code that only detects the presence of any new moving object in the frame.

Working:
  first this code takes a pic of the first frame is seen through your camera and save it as a first_frame, from the next frame, it will compare the first_frame and thee nect frame, if both are same it will be printing the result as normal, if there is any object that is placed in front of the screeen that is not present as first_frame, it will check for the object presence with the help of cv2.findContours function, it will subtract the present frame with the first_frame to detect the position of the object and will draw a box around the objects denoting that they are the new ones.
