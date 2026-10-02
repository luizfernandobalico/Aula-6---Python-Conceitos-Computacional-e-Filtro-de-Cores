import cv2

# Abrir a imagem
imagem = cv2.imread("foto2.jpg")

# Verificar se a imagem foi encontrada
if imagem is None:
    print("Imagem não encontrada!")
else:
    print("Imagem carregada com sucesso!")

    # Mostrar a imagem
    cv2.imshow("Minha Imagem", imagem)

    # Esperar uma tecla
    cv2.waitKey(0)

    # Fechar a janela
    cv2.destroyAllWindows()