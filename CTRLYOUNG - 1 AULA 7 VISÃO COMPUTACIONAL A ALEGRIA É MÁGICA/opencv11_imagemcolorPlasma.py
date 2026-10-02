import cv2

# Abrir a imagem
imagem = cv2.imread("modelo.jpg")

# Converter para tons de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar o filtro PLASMA
imagem_plasma = cv2.applyColorMap(cinza, cv2.COLORMAP_PLASMA)

# Mostrar a imagem
cv2.imshow("Filtro PLASMA", imagem_plasma)

# Salvar a imagem
cv2.imwrite("foto_plasma.jpg", imagem_plasma)

# Esperar uma tecla
cv2.waitKey(0)

# Fechar a janela
cv2.destroyAllWindows()