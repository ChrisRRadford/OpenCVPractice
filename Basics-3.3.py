import cv2
import numpy as np
from matplotlib import pyplot as plt


def Main():
	#Filtering()
	#AvgBlurring()
	#GaussBlurring()
	#MedianBlurring()
	bilateralBlurring()

def Filtering():
	img = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\DeerNoisy.jpg')
	cv2.imshow('Origional',img)
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(img,-1,kernel)
	cv2.imshow('Smoothed',img)
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()

def AvgBlurring():
	img = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\DeerNoisy.jpg')
	cv2.imshow('Origional',img)
	blur3 = cv2.blur(img,(3,3))
	blur9 = cv2.blur(img,(9,9))
	blur15 = cv2.blur(img,(15,15))
	cv2.imshow('Avg3',blur3)
	cv2.imshow('Avg9',blur9)	
	cv2.imshow('Avg15',blur15)		
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()

def GaussBlurring():
	img = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\DeerNoisy.jpg')
	cv2.imshow('Origional',img)
	gaussBlur = cv2.GaussianBlur(img,(5,5),0)
	gaussBlur1 = cv2.GaussianBlur(img,(5,5),10)
	cv2.imshow('Blur',gaussBlur)	
	cv2.imshow('Blur1',gaussBlur1)		
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()	

def MedianBlurring():
	img = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\DeerNoisy.jpg')
	cv2.imshow('Origional',img)
	medianBlur = cv2.medianBlur(img,5)
	medianBlur1 = cv2.medianBlur(img,5)
	cv2.imshow('Blur',medianBlur)	
	cv2.imshow('Blur1',medianBlur1)		
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()	

def bilateralBlurring():
	img = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\DeerNoisy.jpg')
	cv2.imshow('Origional',img)
	biBlur = cv2.bilateralFilter(img,9,175,75)
	cv2.imshow('Blur',biBlur)	
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()	

Main()