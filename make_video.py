#!/usr/bin/python

from multiprocessing import Process, Pipe
import os
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
check_time='minute'

############################

class Record:   # Create the Record class

    # initialize the class variables
    def __init__(self,video_format,video_frame_rate,time_color,time_thickness,video_name,check_time):
        self.video_format=video_format
        self.time_color=time_color
        self.time_thickness=time_thickness
        self.video_name=video_name
        self.video_frame_rate=video_frame_rate
        self.check_time=check_time

    # Record with the gui video player
    def record_function_with_player(self):
        #w=640
        #h=480
        # Print the process id on UNIX and WINDOW
        print ("process id:",os.getpid())
        # Defy the codec and create VideoWriter object
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*self.video_format)
        out = cv2.VideoWriter(self.video_name,fourcc, self.video_frame_rate, (640,480))

        # Memorate the time the video record started
        time_before=datetime.datetime.now()

        time_before_minute=time_before.minute  # Memorate the minute the program started
        time_before_hour=time_before.hour      # Memorate the hour the program started
        time_before_day=time_before.day        # Memorate the day the program started


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

                time_right_now_minute=now.minute     # Memorate the minute for each frame
                time_right_now_hour=now.hour       # Memorate the hour for each frame
                time_right_now_day=now.day        # Memorate the day for each day


                font = cv2.FONT_HERSHEY_SIMPLEX # Choose a font for the time string in the video

                cv2.putText(frame,str(time_right_now_hour),(410,60), font, 0.6,self.time_color,self.time_thickness,cv2.LINE_AA)
                cv2.putText(frame,str(time_on_video_trunchated),(410,20), font, 0.6,self.time_color,self.time_thickness,cv2.LINE_AA) # Atache the time in the upper right of the video
                out.write(frame)              # write the frames and saves them
                cv2.imshow('frame',frame)     # start the video palyer from opencv
                if self.check_time == 'minute':                                     # Checks if the time is set to minutes
                    if str(time_right_now_minute) != str(time_before_minute):       # Checks if it is a different minute since the video recording started
                        break                                                       # If that is true it is stoping the video recording
                elif self.check_time == 'hour':                                     # Checks if the time is set to hours
                    if str(time_right_now_hour) != str(time_before_hour):           # Checks if it is a different hour since the video recording started
                        break                                                       # If that is true it is stoping the video recording
                elif self.check_time == 'day':                                      # Checks if the time is set to days
                    if str(time_right_now_day) != str(time_before_day):             # Checks if it is a different day since the video recording started
                        break                                                       # If that is true it is stoping the video recording

                if cv2.waitKey(1) & 0xFF == ord('q'):    # Checks if the q key from keyboard is pressed
                    break                                # If it is pressed, it is stopping the recording
            else:                                        # If the ret var is not True, it is not recording
                break                                    # Quits the recording process

        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()  # Destroy the window for the player


    # Record without a video player
    def record_function_without_player(self):
        # Print the process id on UNIX and WINDOW
        print ("process id:",os.getpid())
        # Defy the codec and create VideoWriter object
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*self.video_format)
        out = cv2.VideoWriter(self.video_name,fourcc, self.video_frame_rate, (640,480))

        # Memorate the time the video record started
        time_before=datetime.datetime.now()

        time_before_minute=time_before.minute  # Memorate the minute the program started
        time_before_hour=time_before.hour      # Memorate the hour the program started
        time_before_day=time_before.day        # Memorate the day the program started


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

                time_right_now_minute=now.minute     # Memorate the minute for each frame
                time_right_now_hour=now.hour       # Memorate the hour for each frame
                time_right_now_day=now.day        # Memorate the day for each day


                font = cv2.FONT_HERSHEY_SIMPLEX # Choose a font for the time string in the video

                cv2.putText(frame,str(time_right_now_hour),(410,60), font, 0.6,self.time_color,self.time_thickness,cv2.LINE_AA)
                cv2.putText(frame,str(time_on_video_trunchated),(410,20), font, 0.6,self.time_color,self.time_thickness,cv2.LINE_AA) # Atache the time in the upper right of the video
                out.write(frame)              # write the frames and saves them

                if self.check_time == 'minute':                                     # Checks if the time is set to minutes
                    if str(time_right_now_minute) != str(time_before_minute):       # Checks if it is a different minute since the video recording started
                        break                                                       # If that is true it is stoping the video recording
                elif self.check_time == 'hour':                                     # Checks if the time is set to hours
                    if str(time_right_now_hour) != str(time_before_hour):           # Checks if it is a different hour since the video recording started
                        break                                                       # If that is true it is stoping the video recording
                elif self.check_time == 'day':                                      # Checks if the time is set to days
                    if str(time_right_now_day) != str(time_before_day):             # Checks if it is a different day since the video recording started
                        break                                                       # If that is true it is stoping the video recording


            else:                                        # If the ret var is not True, it is not recording
                break                                    # Quits the recording process

        # Release everything if job is finished
        cap.release()
        out.release()






if __name__=="__main__":
    # Create the Record object and pass the global arguments to its class
    create_record=Record(video_format,video_frame_rate,time_color,time_thickness,video_name,check_time)
    #Start the Record process
    first_procees=Process(target=create_record.record_function_with_player)

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
