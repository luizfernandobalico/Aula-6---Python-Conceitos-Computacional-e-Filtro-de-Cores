import cv2

# Abre a câmera
camera = cv2.VideoCapture(0)

while True:
    # Captura o vídeo
    sucesso, imagem = camera.read()

    if not sucesso:
        print("Não foi possível acessar a câmera!")
        break

    # Mostra a imagem da câmera
    cv2.imshow("Minha Camera", imagem)

    # Pressione ESC para sair
    if cv2.waitKey(1) == 27:
        break

# Libera a câmera
camera.release()
cv2.destroyAllWindows()
#Como funciona
import cv2 → importa o OpenCV.
cv2.VideoCapture(0) → acessa a câmera principal do computador.
camera.read() → captura cada imagem da câmera.
cv2.imshow() → mostra a imagem em uma janela.
cv2.waitKey(1) → verifica se alguma tecla foi pressionada.
camera.release() → libera a câmera.
#ESC → fecha o programa.
#Se você tiver mais de uma câmera

#Experimente trocar:

#camera = cv2.VideoCapture(0)

#por:

#camera = cv2.VideoCapture(1)

#ou:

#camera = cv2.VideoCapture(2)

