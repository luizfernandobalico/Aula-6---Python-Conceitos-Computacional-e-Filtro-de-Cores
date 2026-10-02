import cv2
camera = cv2.VideoCapture(0)
while True:
    success, frame = camera.read()            # success será True caso a câmera seja encontrada
    if not success or frame is None:          # Se não encontrar a câmera ou o frame, o laço é encerrado
        break
    cv2.imshow("Acessando Webcam", frame)     # Título da janela
    if cv2.waitKey(1) == 27:                  # Tecla 27 = ESC
        break
camera.release()                              # Libera a câmera
cv2.destroyAllWindows()                       # Fecha todas as janelas
if cv2.waitKey(1) & 0xFF == ord('q'):
    break