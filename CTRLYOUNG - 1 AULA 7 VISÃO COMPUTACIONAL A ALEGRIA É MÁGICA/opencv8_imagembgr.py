import cv2

# Abrir a imagem
imagem = cv2.imread("modelo.jpg")

# Converter BGR para RGB
rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Converter novamente RGB para BGR
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

# Mostrar a imagem
cv2.imshow("Imagem BGR", bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
