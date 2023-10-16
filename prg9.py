import cv2
path ="C:/Users/91956/Downloads/land/GDL/class 1/download (16).png"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)
