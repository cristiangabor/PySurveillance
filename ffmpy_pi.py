import numpy
import cv2
import sys
import subprocess as sp


cap=cv2.VideoCapture(0) # Make a VideoCapture object. The 0 is the argument for the cammera



#firscommand=sys.argv[0]
#secondcommand=sys.argv[1]
#thirdcommand=sys.argv[2]

#sys.exit("gata")

#print (firscommand)
#print (secondcommand)
#print (thirdcommand)

fps=str(cap.get(cv2.CAP_PROP_FPS))
print(fps)
f_format='brg24'
ret,frame=cap.read()
h,w,ch=frame.shape
print(h,w,ch)
dimension='{}x{}'.format(w,h)

command=['ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-c:v','rawvideo',
        '-s', dimension,
        '-pix_fmt', 'bgr24',
        '-r', '24',
        '-i', '-',
        '-an',
        '-c:v', 'libx264',
        '-b:v', '5000k',
        'output_file.mp4']

proces=sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)
va=1
while (True):
	# Capture frame-by-frame
	ret, frame=cap.read()


	# Our operations on the frame come here
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#if va==1:
	proces.stdin.write(frame.tostring())
	#va=0
	#Display the resulting frame

	cv2.imshow('frame',frame	)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	# When everthing done, release the capture

cap.release()
proces.stdin.close()
proces.stderr.close()
cv2.destroyAllWindows()
