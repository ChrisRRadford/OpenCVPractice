import cv2
import numpy as np


def Main():
	CirclesAndSquares()

def Circles():	
	global img 
	img = np.zeros((512,512,3), np.uint8)
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',DrawCircle)
	while(1):
		cv2.imshow('image',img)
		if cv2.waitKey(1) & 0xFF == 27:
			break
	cv2.destroyAllWindows()

def DrawCircle(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),100,(255,0,0),-1)


def CirclesAndSquares():
	global img, drawing, mode, ix, iy
	drawing = False
	mode = True
	ix, iy = -1,-1
	img = np.zeros((512,512,3), np.uint8)
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',DrawCircleOrSquare)

	while(1):
	    cv2.imshow('image',img)
	    k = cv2.waitKey(1) & 0xFF
	    if k == ord('m'):
	        mode = not mode
	    elif k == 27:
	        break

	cv2.destroyAllWindows()

def DrawCircleOrSquare(event,x,y,flags,param):
	global img, drawing, mode, ix, iy
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
			else:
				cv2.circle(img,(x,y),5,(0,0,255),-1)

	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
		else:
			cv2.circle(img,(x,y),5,(0,0,255),-1)

Main()



