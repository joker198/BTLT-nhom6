import cv2
import matplotlib
import numpy as np

# tao anh moi
height = width = 400
image501 = np.zeros((height,width,3), np.uint8)

# dien mau cho tung pixel
for r in range (0,width):
	for c in range (0,height):
		if((((r//50)%2)+((c//50)%2))%2)==1:
			image501[r:r+1,c:c+1] = (255,255,255)
			pass
		else:
			image501[r:r+1,c:c+1] = (0,0,0)
			pass
		pass
	pass

cv2.imshow('anh ban co vua: ', image501)
#save image
cv2.imwrite("image501.jpg",image501 )

cv2.waitKey(0)
cv2.destroyAllWindows()

