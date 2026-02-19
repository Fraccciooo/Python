# Manera anfibia, usando muchas lineas de codigo, funiones atras de la otra
# se utilizan 5 lineas de codigo para convertir un numero a su valor absoluto y redondearlo, 
# pero se puede hacer todo en una sola linea utilizando funciones anidadas

num = input("Digita un numero: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# Manera mas eficiente, utilizando funciones anidadas, es decir, 
# utilizando una funcion dentro de otra

# Se coloca cada funcion dentro de la otra, haciendo que el resultado sea el mismo
# pero mas eficiente, se utiliza una sola linea de codigo
print(round(abs(float(input("Digita un numero: ")))))

# -------NOTA-------
# El dato que el usuario ingrese se guarda momentaneamente en la memoria, 
# y se va pasando de una funcion a otra, una vez que se muestra el resultado, 
# el dato se borra de la memoria, es decir, no queda guardado en ninguna variable,