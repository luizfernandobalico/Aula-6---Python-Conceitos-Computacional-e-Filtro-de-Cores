import cv2

# Abrir a imagem
imagem = cv2.imread("ImgOvelhas.jpg")

# Converter para escala de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Mostrar a imagem
cv2.imshow("Imagem em Cinza", cinza)

# Esperar uma tecla
cv2.waitKey(0)

# Fechar a janela
cv2.destroyAllWindows()