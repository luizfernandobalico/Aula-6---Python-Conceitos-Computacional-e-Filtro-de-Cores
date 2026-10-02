import cv2

camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()

    if not sucesso:
        break

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(cinza, 100, 200)

    cv2.imshow("Camera", frame)
    cv2.imshow("Filtro Canny", canny)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()