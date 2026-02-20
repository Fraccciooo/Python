texto = "ya estas progresando y no te das cuenta"

with open("texto_2.txt", "a") as file:
    file.write(texto)
    file.close()
