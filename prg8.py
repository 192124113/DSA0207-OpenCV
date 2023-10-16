import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("C:/Users/91956/Downloads/land/GDL/class 1/download (16).png",cv2.IMREAD_COLOR)
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
