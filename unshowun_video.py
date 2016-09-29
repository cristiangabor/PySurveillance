import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)


bluecolor=(255,2,0)


# Define the codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (640,480))

while(True):
    
    ret, frame = cap.read()
    
    if ret==True:
        
        # Use the datetime function to display it on the video
        
        time=datetime.datetime.now()

        # truncate the original string in a shorter one

        time2=''
        for i in str(time):
            if len(time2)==19:
                break
            else:
                time2+=str(i)

        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.putText(frame,str(time2),(410,20), font, 0.6,bluecolor,2,cv2.LINE_AA)
        # write the flipped frame
        out.write(frame)

        
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()