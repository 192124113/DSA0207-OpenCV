import cv2
img1 = cv2.imread("C:/Users/91956/Downloads/images.png")
img2 = cv2.imread("C:/Users/91956/OneDrive/Pictures/Screenshots/Screenshot 2023-10-16 125614.png")
(x1, y1) = (100, 100)
(x2, y2) = (300, 300)
cropped_img1 = img1[y1:y2, x1:x2]
copied_img1 = cropped_img1.copy()
(x, y) = (100, 100)
img2[y:y + copied_img1.shape[0], x:x + copied_img1.shape[1]] = copied_img1
cv2.imshow("Output Image", img2)
cv2.waitKey(0)
