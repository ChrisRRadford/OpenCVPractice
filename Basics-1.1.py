import numpy as np
import cv2

def Main():
	#img = cv2.resize(cv2.imread('/Users/chrisradford/Documents/Research/avanetics-5775d1/_DSC0061.jpg',1),(1200,900))
	img = cv2.resize(cv2.imread('/Users/chrisradford/Documents/Research/ImagesToPass/image1.jpg',1),(1200,900))	
	cv2.imshow('image',img)
	cv2.waitKey(0)
	#cv2.destroyNamedWindow('images')

def SaveOrDelGrayScale():
	img = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\camps.jpg',0)
	cv2.imshow('Image GrayScale',img)
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()
	elif(key == ord('s')):
		cv2.imwrite('C:\Users\cradford\Documents\Research\Test Images\camps_Gray.jpg',img)

#SaveOrDelGrayScale()
Main()