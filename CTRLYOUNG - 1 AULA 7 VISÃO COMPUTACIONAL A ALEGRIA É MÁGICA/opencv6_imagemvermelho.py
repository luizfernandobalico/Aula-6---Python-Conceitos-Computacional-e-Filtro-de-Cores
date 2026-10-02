import cv2

# Abrir a imagem
imagem = cv2.imread("ImgOvelhas.jpg")

# Criar uma camada vermelha
vermelho = imagem.copy()
vermelho[:, :] = (0, 0, 255)

# Misturar a imagem com a cor vermelha
resultado = cv2.addWeighted(imagem, 0.2, vermelho, 0.8, 0)

# Mostrar
cv2.imshow("Imagem Vermelha", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()