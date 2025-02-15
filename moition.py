import cv2
import numpy as np


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

prev_frame = None #This is so we can store the previous frame

while True:
    ret, frame = cap.read()

    #if we dont get any signal from camera we send a could not read frame error
    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)  # This is to create a mirror effect you can comment it out if you dont want it

    if prev_frame is not None:
        # Invert the delayed frame
        inverted_prev_frame = cv2.bitwise_not(prev_frame)

        # Mix the previous frame and the current frame by setting the opacity to 50% and this would make a gray color
        blended_frame = cv2.addWeighted(frame, 0.5, inverted_prev_frame, 0.5, 0)

        # Display the blended output
        cv2.imshow("Blended Video (Inverted Delayed Layer)", blended_frame)
        
    else:
       #we need this for the first frame because when it has none initally it wont work 
        # Display normal frame on the first iteration
        cv2.imshow("Blended Video (Inverted Delayed Layer)", frame)

    # This is to move the current frame to the past frame 
    prev_frame = frame.copy()

    # Prese the key 'q' to exit to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
