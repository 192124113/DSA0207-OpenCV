import cv2
car_cascade = cv2.CascadeClassifier("C:/Users/91956/Downloads/cars.xml")
cap = cv2.VideoCapture("C:/Users/91956/Downloads/WhatsApp Video 2023-10-18 at 08.28.48_39a7379e.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(20, 20))
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
