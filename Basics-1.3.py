import numpy as np
import cv2

def Main():
	#DrawLine()
	#DrawRectangle()
	#DrawCircle()
	#DrawEllipse()
	#DrawPolygon()
	PutText()

def DrawLine():
	img = np.zeros((512,512,3), np.uint8)
	cv2.line(img,(0,0),(511,511),(255,0,0),5) #(source, starting point, end point, color(BGR),thickness)
	cv2.imshow('line',img)
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()

def DrawRectangle():
	img = np.zeros((512,512,3), np.uint8)
	cv2.rectangle(img,(384,300),(510,350),(0,200,0),3) #(source, starting point(TL), end point(BR), color(BGR),thickness)
	cv2.imshow('rectangle',img)
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()

def DrawCircle():
	img = np.zeros((512,512,3), np.uint8)
	cv2.circle(img,(250,100),63,(0,0,255),5) #(source, starting point(TL), radius, color(BGR),thickness(-1 = fill))
	cv2.imshow('circle',img)
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()

def DrawEllipse():
	img = np.zeros((512,512,3), np.uint8)
	cv2.ellipse(img,(256,256),(100,50),0,180,360,(0,255,0),1) #(source, center location(x,y), axes length(major,minor),angle of rotation, start angle, end andlge,color,fill)
	cv2.imshow('ellipse',img)
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()

def DrawPolygon():
	img = np.zeros((512,512,3), np.uint8)
	pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
	pts = pts.reshape(-1,1,2)
	cv2.polylines(img,[pts],True,(0,255,255)) # (source, point list, True = connect first and last point, color)
	cv2.imshow('ellipse',img)
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()

def PutText():
	img = np.zeros((512,512,3), np.uint8)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,'Learning Stuff',(30,450), font, 2,(255,255,255),8,cv2.LINE_AA)
	cv2.imshow('Text',img)
	key = cv2.waitKey(0) & 0xFF
	if(key == 27):
		cv2.destroyAllWindows()

Main()