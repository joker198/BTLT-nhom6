import cv2
import matplotlib
import numpy as np
import colorsys


# tao anh moi
height = width = 330
image503 = np.zeros((height,width,3), np.uint8)


# dien mau cho tung pixel
for r in range (0,height):
	a = colorsys.hsv_to_rgb(r/360.0,1,1)   # conver mau tu hsv sang rgb
	b = (a[2]*255,a[1]*255,a[0]*255) 
	for c in range (0,width): 
		image503[r:r+1,c:c+1] = b	

cv2.imshow('dai mau tuan tu theo chieu doc tu do den tim: ', image503)
#save image
cv2.imwrite("image503.jpg",image503 )

cv2.waitKey(0)
cv2.destroyAllWindows()

