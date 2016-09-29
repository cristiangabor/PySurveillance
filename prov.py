import sys

ACCEPT='NO'
VERSION='1.0'
NAME='PySurveillance'
MADE_BY='Cristian Gabor'




b=len(sys.argv)

for i in range(b-1):
	value_of_parameters=sys.argv[i+1]

	if ( str(value_of_parameters)=='-v' ):
		print("Version",VERSION,'of', NAME,'made by',MADE_BY)
	elif str(value_of_parameters)=='-d':
		try:
			record_path=sys.argv[i+2]
			print(record_path)
		except:
			print ("the path for -d parameter dosen't exit!")
	elif str(value_of_parameters)=='-f':
		try:
			video_record_format=sys.argv[i+2]
			print (video_record_format)
		except:
			print ("The video format is not corect added")
	elif str(value_of_parameters)=='-c':
		try:
			text_video_color=sys.argv[i+2]
			print (text_video_color)
		except:
			print ("The color is not specified!")
	elif str(value_of_parameters)=='-t':
		try:
			time_of_video=sys.argv[i+2]
			print (time_of_video)
		except:
			print("The time is not specified!")
	elif str(value_of_parameters)=='-r':
		try:
			frame_rate=sys.arg[i+2]
			print(frame_rate)
		except:
			print("The frame rate is not specified!")
	elif str(value_of_parameters)=='-w':
		try:
			width_and_height=sys.argv[i+2]
			print(width_and_height)
		except:
			print("The video width and height is not specified!" )
#	else:
#		message_info=open('info.txt','r')
#		print_message_info=message_info.read()

#		print(print_message_info)
#		message_info.close()
#		break
