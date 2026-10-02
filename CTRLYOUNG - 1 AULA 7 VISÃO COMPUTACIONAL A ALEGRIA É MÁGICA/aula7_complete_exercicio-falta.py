if not smile:
    print("Sorrisos? Nada ainda?")

elif not eyes:
    print("Olhos? Nada ainda???")

else:
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Filtro de cinza