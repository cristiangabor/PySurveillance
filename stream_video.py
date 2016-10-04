import numpy
import cv2
import sys
import subprocess as sp


cap=cv2.VideoCapture(0) # Make a VideoCapture object. The 0 is the argument for the cammera



fps=str(cap.get(cv2.CAP_PROP_FPS)) # get the frames per second from the opencv
print(fps)                         # print it to screen
f_format='brg24'                   # defy the color scheme
ret,frame=cap.read()               # read one frame
h,w,ch=frame.shape                 # take the height , width and channel (3) from the frame
print(h,w,ch)                      # print them
dimension='{}x{}'.format(w,h)      # merge those two dimensions
FFMPEG='ffmpeg'                    # defy the Ffmpeg arguments

command=[FFMPEG,
        '-re',                     # this argument is for updating the existent video file (optional)
        '-f', 'rawvideo',          # the format. In this case thakes the raw format from opencv
        '-c:v','rawvideo',         # the video codec is not defined. It takes the raw format from frames
        '-s', dimension,           # the dimenisons of the frame
        '-pix_fmt', 'bgr24',       # pixel format
        '-r', '24',                # frame rate
        '-i', '-',                 # it takes the video input from a pipe
        '-an',                     # for now, it takes only the video from the opencv
        '-c:v', 'libx264',         # is making the video conversion into the specified fromat
        '-b:v', '5000k','-f',      # the bitrate (5000k)
        'flv',
        'rtmp://localhost/myapp/mystream']              # the video file name


# Defy the process and link the stdin and sterr trought an external pipe
proces=sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

while (True):
	# Capture frame-by-frame
	ret, frame=cap.read()
	proces.stdin.write(frame.tostring())       # takes the frames from opencv and troughs it to a pipe in ffmpeg

	#Display the resulting frame
	cv2.imshow('frame',frame	)
	if cv2.waitKey(1) & 0xFF == ord('q'):      # wait for q to be preesed to close the windows
		break

	# When everthing done, release the capture

cap.release()
proces.stdin.close()
proces.stderr.close()
cv2.destroyAllWindows()
