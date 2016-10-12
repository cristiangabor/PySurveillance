#!/usr/bin/python

from multiprocessing import Process, Pipe
import os
import subprocess as sp
import numpy as np
import cv2
import datetime
import time
import sys

# defy the video parameters
video_format='XVID'
time_color=(255,255,255 )
time_thickness=2
video_name='/home/cristian/cristi.avi'
video_frame_rate=20.0
check_time='day'
video_height=640
video_width=480

############################

class Record:   # BOOM! The Record class

    # initialize the class variables
    def __init__(self,video_format,video_frame_rate,time_color,time_thickness,video_name,check_time,video_height,video_width):
        self.video_format=video_format
        self.time_color=time_color
        self.time_thickness=time_thickness
        self.video_name=video_name
        self.video_frame_rate=video_frame_rate
        self.check_time=check_time
        self.video_height=video_height
        self.video_width=video_width


    def make_thestreamhappen(self,video_height,video_width):
        # the brg24 format is used to keep the good coloration for the streamed video
        f_format='brg24'                                        # defy the color scheme
        dimension='{}x{}'.format(video_height,video_width)      # merge those two dimensions
        FFMPEG='ffmpeg'                                         # defy the Ffmpeg arguments

        command=[FFMPEG,
                '-re',                                # this argument is for updating the existent video file (optional)
                '-f', 'rawvideo',                     # the format. In this case thakes the raw format from opencv
                '-c:v','rawvideo',                    # the video codec is not defined. It takes the raw format from frames
                '-s',dimension,                       # the dimenisons of the frame
                '-pix_fmt','bgr24',                   # pixel format
                '-r','24',                            # frame rate
                '-i','-',                             # it takes the video input from a pipe
                '-an',                                # for now, it takes only the video from the opencv
                '-c:v', 'libx264',                    # is making the video conversion into the specified fromat
                '-b:v', '5000k','-f',                 # the bitrate (5000k)
                'flv',                                # output format is flv
                'rtmp://localhost/myapp/mystream']    # stream the video output

        return command

    # Record with the gui video playe
    def record_and_stream(self):

        # Print the process id on UNIX and WINDOW
        print ("\nThe id process:",os.getpid(),"started!\n")
        # Defy the codec and create VideoWriter object
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*self.video_format)
        out = cv2.VideoWriter(self.video_name,fourcc, self.video_frame_rate, (self.video_height,self.video_width))

        # Memorate the time the video record started
        time_before=datetime.datetime.now()


        command_to_start = self.make_thestreamhappen(self.video_height,self.video_width)
        proces=sp.Popen(command_to_start, stdin=sp.PIPE, stderr=sp.PIPE)


        # Start frame recording
        while(True):

            ret, frame = cap.read()   # The ret var is boolean

            if ret==True:

                time_on_the_video=datetime.datetime.now()   # Use the datetime function to display it on the video
                time_on_video_trunchated=''                 # Truncate the original string in a shorter one
                for i in str(time_on_the_video):
                    if len(time_on_video_trunchated)==19:
                        break
                    else:
                        time_on_video_trunchated+=str(i)

                # Memorate the time for each frame
                now=datetime.datetime.now()

                font = cv2.FONT_HERSHEY_SIMPLEX # Choose a font for the time string in the video

                cv2.putText(frame,str(time_on_video_trunchated),(410,20), font, 0.6,self.time_color,self.time_thickness,cv2.LINE_AA) # Atache the time in the upper right of the video
                proces.stdin.write(frame.tostring())

                out.write(frame)              # write the frames and saves them
                cv2.imshow('frame',frame)     # start the video palyer from opencv
                if self.check_time == 'minute':                                     # Checks if the time is set to minutes
                    past_time=time_before + datetime.timedelta(minutes=1)
                    if now > past_time:       # Checks if it is a different minute since the video recording started
                        break                                                       # If that is true it is stoping the video recording
                elif self.check_time == 'hour':
                    past_time=time_before + datetime.timedelta(hours=1)
                    if now > past_time:
                        break                                                       # Checks if the time is set to hours
                elif self.check_time == 'day':
                    past_time=time_before + datetime.timedelta(days=1)              # Checks if the time is set to days
                    if now > past_time:                                             # Checks if it is a different day since the video recording started
                        break                                                       # If that is true it is stoping the video recording

                if cv2.waitKey(1) & 0xFF == ord('q'):    # Checks if the q key from keyboard is pressed
                    break                                # If it is pressed, it is stopping the recording
            else:                                        # If the ret var is not True, it is not recording
                break                                    # Quits the recording process

        # Release everything if job is finished
        cap.release()
        out.release()
        proces.stdin.close()
        proces.stderr.close()
        cv2.destroyAllWindows()  # Destroy the window for the player

    def record_and_show(self):

        # Print the process id on UNIX and WINDOW
        print ("\nThe id process:",os.getpid(),'started!\n')
        # Defy the codec and create VideoWriter object
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*self.video_format)
        out = cv2.VideoWriter(self.video_name,fourcc, self.video_frame_rate, (640,480))

        # Memorate the time the video record started
        time_before=datetime.datetime.now()

        # Start frame recording
        while(True):

            ret, frame = cap.read()   # The ret var is boolean

            if ret==True:

                time_on_the_video=datetime.datetime.now()   # Use the datetime function to display it on the video
                time_on_video_trunchated=''                 # Truncate the original string in a shorter one
                for i in str(time_on_the_video):
                    if len(time_on_video_trunchated)==19:
                        break
                    else:
                        time_on_video_trunchated+=str(i)

                # Memorate the time for each frame
                now=datetime.datetime.now()


                font = cv2.FONT_HERSHEY_SIMPLEX # Choose a font for the time string in the video

                cv2.putText(frame,str(time_on_video_trunchated),(410,20), font, 0.6,self.time_color,self.time_thickness,cv2.LINE_AA) # Atache the time in the upper right of the video
                out.write(frame)              # write the frames and saves them
                cv2.imshow('frame',frame)     # start the video palyer from opencv
                if self.check_time == 'minute':                                     # Checks if the time is set to minutes
                    past_time=time_before + datetime.timedelta(minutes=1)
                    if now > past_time:       # Checks if it is a different minute since the video recording started
                        break                                                       # If that is true it is stoping the video recording
                elif self.check_time == 'hour':
                    past_time=time_before + datetime.timedelta(hours=1)
                    if now > past_time:
                        break                                                       # Checks if the time is set to hours
                elif self.check_time == 'day':
                    past_time=time_before + datetime.timedelta(days=1)              # Checks if the time is set to days
                    if now > past_time:                                             # Checks if it is a different day since the video recording started
                        break                                                       # If that is true it is stoping the video recording

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()  # Destroy the window for the player


    # Record without a video player
    def only_record(self):
        # Print the process id on UNIX and WINDOW
        print ("\n The id process:",os.getpid(),'started!\n')
        # Defy the codec and create VideoWriter object
        cap = cv2.VideoCapture(0)

        # Memorate the time the video record started
        time_before=datetime.datetime.now()



        # Start frame recording
        while(True):

            ret, frame = cap.read()   # The ret var is boolean

            if ret==True:

                time_on_the_video=datetime.datetime.now()   # Use the datetime function to display it on the video
                time_on_video_trunchated=''                 # Truncate the original string in a shorter one
                for i in str(time_on_the_video):
                    if len(time_on_video_trunchated)==19:
                        break
                    else:
                        time_on_video_trunchated+=str(i)

                # Memorate the time for each frame
                now=datetime.datetime.now()
                font = cv2.FONT_HERSHEY_SIMPLEX # Choose a font for the time string in the video
                cv2.putText(frame,str(time_on_video_trunchated),(410,20), font, 0.6,self.time_color,self.time_thickness,cv2.LINE_AA) # Atache the time in the upper right of the video



                if self.check_time == 'minute':                                     # Checks if the time is set to minutes
                    past_time=time_before + datetime.timedelta(minutes=1)
                    if now > past_time:       # Checks if it is a different minute since the video recording started
                        break                                                       # If that is true it is stoping the video recording
                elif self.check_time == 'hour':
                    past_time=time_before + datetime.timedelta(hours=1)
                    if now > past_time:
                        break                                                       # Checks if the time is set to hours
                elif self.check_time == 'day':
                    past_time=time_before + datetime.timedelta(days=1)              # Checks if the time is set to days
                    if now > past_time:                                             # Checks if it is a different day since the video recording started
                        break                                                       # If that is true it is stoping the video recording


            else:                                        # If the ret var is not True, it is not recording
                break                                    # Quits the recording process

        # Release everything if job is finished
        cap.release()
        out.release()



if __name__=="__main__":
    # Create the Record object and pass the global arguments to its class
    create_record=Record(video_format,video_frame_rate,time_color,time_thickness,video_name,check_time,video_height,video_width)
    #Start the Record process
    first_procees=Process(target=create_record.record_and_stream)

    start_recording=input("Start the video recording? (y/n):")
    if str(start_recording) =='y':
        first_procees.start()
        while(True):
            terminate_process=input("quit(y/n):")
            if str(terminate_process)=="y":
                first_procees.terminate()

            else:
                print ("continue")
            if str(terminate_process)=='z':
                break

    else:
        print ("Ok then")
