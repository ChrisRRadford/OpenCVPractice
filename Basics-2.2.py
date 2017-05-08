import cv2
import numpy as np

img1 = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\Scatter1.png')
img2 = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\Scatter1.png')
img3 = cv2.imread('C:\Users\cradford\Documents\Research\Test Images\Scatter1.png')

#cv2.imshow('image1',img1)
#cv2.imshow('image2',img2)
#add = img1 + img2
#add = cv2.add(img1,img2)
weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
