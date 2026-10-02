import cv2

# 1. Carregar a foto
foto = cv2.imread("foto.jpg")

# 2. Converter a foto para tons de cinza
cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

# 3. Aplicar o filtro Canny
canny = cv2.Canny(cinza, 100, 200)

# 4. Mostrar a foto original
cv2.imshow("Foto Original", foto)

# 5. Mostrar a foto com Canny
cv2.imshow("Filtro Canny", canny)

# 6. Esperar uma tecla
cv2.waitKey(0)

# 7. Fechar as janelas
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()

