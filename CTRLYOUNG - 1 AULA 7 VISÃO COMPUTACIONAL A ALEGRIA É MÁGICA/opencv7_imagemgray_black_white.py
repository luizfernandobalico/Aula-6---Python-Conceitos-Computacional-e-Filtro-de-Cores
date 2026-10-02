import cv2
import numpy as np

# Abrir a imagem
imagem = cv2.imread("ImgOvelhas.jpg")

# Converter de BGR para HSV
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Limites para procurar a cor cinza
limite_baixo = np.array([0, 0, 50])
limite_alto = np.array([180, 50, 200])

# Criar máscara
mascara = cv2.inRange(hsv, limite_baixo, limite_alto)

# Mostrar resultado
cv2.imshow("Imagem Original", imagem)
cv2.imshow("Cinza Encontrado", mascara)

cv2.waitKey(0)
cv2.destroyAllWindows()