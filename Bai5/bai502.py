import cv2
import matplotlib
import numpy as np
import colorsys


# tao anh moi
height = width = 330
image502 = np.zeros((height,width,3), np.uint8)


# dien mau cho tung pixel
for c in range (0,width):
	a = colorsys.hsv_to_rgb(c/360.0,1,1)   # conver mau tu hsv sang rgb
	b = (a[2]*255,a[1]*255,a[0]*255) 
	for r in range (0,height): 
		image502[r:r+1,c:c+1] = b	

cv2.imshow('dai mau tuan tu theo chieu ngang tu do den tim : ', image502)
#save image
cv2.imwrite("image502.jpg",image502 )

cv2.waitKey(0)
cv2.destroyAllWindows()

