import cv2

# Abrir a imagem
imagem = cv2.imread("foto.jpg")

# Criar uma camada azul do mesmo tamanho da imagem
azul = imagem.copy()
azul[:, :] = (0,0,128)  # Azul no formato BGR do OpenCV

# Misturar a foto com a camada azul
resultado = cv2.addWeighted(imagem, 0.3, azul, 0.7, 0)

# Mostrar a imagem
cv2.imshow("Imagem Azul", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()