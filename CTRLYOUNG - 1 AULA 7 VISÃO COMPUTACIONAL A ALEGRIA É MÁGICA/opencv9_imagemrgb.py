import cv2

imagem = cv2.imread("modelo.jpg")

# Trocar BGR para RGB
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

cv2.imshow("Imagem", imagem_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()