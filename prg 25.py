import cv2
import numpy as np
image = cv2.imread("C:/Users/91956/Downloads/images.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
horizontal_gradient = np.array([[-1, -2, -1],
                                [0, 0, 0],
                                [1, 2, 1]], dtype=np.float32)
vertical_gradient = np.array([[-1, 0, 1],
                              [-2, 0, 2],
                              [-1, 0, 1]], dtype=np.float32)
gradient_x = cv2.filter2D(gray_image, -1, horizontal_gradient)
gradient_y = cv2.filter2D(gray_image, -1, vertical_gradient)
sharpened_image = cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)
sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('sharpened_image.jpg', sharpened_image)
