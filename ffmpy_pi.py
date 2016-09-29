import numpy 
import cv2
import sys

cap=cv2.VideoCapture(0) # Make a VideoCapture object. The 0 is the argument for the cammera



firscommand=sys.argv[0]
secondcommand=sys.argv[1]
thirdcommand=sys.argv[2]

sys.exit("gata")

print (firscommand)
print (secondcommand)
print (thirdcommand)

while (True):
	# Capture frame-by-frame
	ret, frame=cap.read()


	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	#Display the resulting frame

	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	# When everthing done, release the capture

cap.release()
cv2.destroyAllWindows()


