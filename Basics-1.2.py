import numpy as np
import cv2

def Main():
	SaveVideo()

def Video():
	cap = cv2.VideoCapture(0)
	while(True):
		#capture frame-by-frame from video camera
		#must always have ret, frame but don't know why
		ret, frame = cap.read()

		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		# Diplay the resulting frame
		cv2.imshow('frame-Gray',gray)
		frame = cv2.flip(frame,1)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

def PlayVideo():
	cap = cv2.VideoCapture(0)
	while(True):
		ret, frame = cap.read()
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()

def SaveVideo():
	cap = cv2.VideoCapture(0)

	#define video oject
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

	while(cap.isOpened()):
		ret, frame = cap.read()
		if (ret == True):
			frameflip = cv2.flip(frame,1)

			#write flipped frame
			out.write(frame)

			cv2.imshow('frame',frame)
			cv2.imshow('frameflip',frameflip)
			if (cv2.waitKey(1) & 0xFF == ord('q')):
				break
		else:
			break

	cap.release()
	out.release()
	cv2.destroyAllWindows()

Main()