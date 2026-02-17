nombre = ""
telefono = "0424-1266232"

# Con la Declaracion "BREAK", la funcion unica es poder romper el bucle con alfuna condicion
# en este caso, si el usuario ingresa su nombre, se rompe el ciclo
while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre != "":
        break

print(f"Tu nombre es: {nombre}")

# Pasando a la siguiente declaracion nos encontramos con "CONTINUE"
# que no que hace es ignorar alfun caracter mediante alguna condicion
# se ignora el simbolo "-" para poder dar el telefono solo con datos numericos 
for i in telefono:
    if i == "-":
        continue   
    print(i, end="")

# Y por ultimo tenemos el "PASS", que tiene como funcion dar por alto algun caracter
# en este caso se salta el numero 13, haciendo que la secuencia sea:
# ...9, 10, 11, 12, "-*-", 14, 15...
for i in range(1,20):
    if i == 13:
        print("-*-")
        pass
    else:
        print(i)