import cv2
import matplotlib
import numpy as np
import colorsys


# tao anh moi
height = width = 330
image504 = np.zeros((height,width,3), np.uint8)


# dien mau cho tung pixel
for r in range (0,height):
	for c in range (0,width):
		a = colorsys.hsv_to_rgb((r+c)/(2*360.0),1,1)   # conver mau tu hsv sang rgb
		b = (a[2]*255,a[1]*255,a[0]*255) 
		image504[r:r+1,c:c+1] = b	

cv2.imshow('dai mau tuan tu theo chieu cheo tu do den tim: ', image504)
#save image
cv2.imwrite("image504.jpg",image504 )

cv2.waitKey(0)
cv2.destroyAllWindows()

