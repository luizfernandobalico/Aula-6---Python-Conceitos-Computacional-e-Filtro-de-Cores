import cv2
import time

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
smile_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

eye_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)
while True:
    success, frame = camera.read()

    if not success or frame is None:
        break

    detectou_sorriso = False
    detectou_olhos = False

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:
        eyes_region_gray = gray[y:y + h // 2, x:x + w]   
        face_gray = gray[y:y + h, x:x + w]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        eyes = eye_detector.detectMultiScale(
            eyes_region_gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(25, 25)
            )
        smiles = smile_detector.detectMultiScale(
            face_gray,
            scaleFactor=1.7,
            minNeighbors=20,
            minSize=(25, 25)
            )

        if len(eyes) > 0:
            detectou_olhos = True

        if len(smiles) > 0:
            detectou_sorriso = True
    if detectou_sorriso:
        frame = cv2.applyColorMap(frame, cv2.COLORMAP_SPRING)
        cv2.putText(frame,
                "A ALEGRIA É MÁGICA!",
                (20, 80),
                cv2.FONT_HERSHEY_DUPLEX,
                1.5,
                (255, 255, 255),
                3)
    elif detectou_olhos: 
        edges = cv2.Canny(frame, 100, 200)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    else: 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Visão Computacional em Python !! :D ", frame)
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
