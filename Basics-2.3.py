import numpy as np
import cv2


def Mian():
	HowLong()


def HowLong():
	e1 = cv2.getTickCount()
	img = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\camps.jpg',1)
	cv2.imshow('image',img)
	e2 = cv2.getTickCount()
	time = (e2-e1)/ cv2.getTickFrequency()
	print time
	cv2.waitKey(0)	
	cv2.destroyAllWindows()



Main()