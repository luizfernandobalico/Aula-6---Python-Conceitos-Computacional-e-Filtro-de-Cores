import cv2
import time
camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success or frame is None:
        break

    cv2.imshow("Visão Computacional em Python !! :D ", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()