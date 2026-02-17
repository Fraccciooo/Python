edad = input("Ingrese su edad: ")
edad = int(edad)

try:
    # Primero se coloca la condicion no que NO se quiere lograr
    # en este caso, se requie que el usuario tenga mas de 18 años
    if edad < 18:
        print("Eres menor de edad.")
    # Luego se colocan las condiciones que se quieren lograr
    # en este caso, se requiere que el usuario tenga entre 18 y 65 años
    elif edad < 65:
        print("Eres adulto.")
    # Finalmente, se coloca la condicion que se quiere lograr 
    # en caso de que ninguna de las anteriores se cumpla
    else:
        print("Eres adulto mayor.")
except ValueError:
    print("Por favor, ingresa un número válido.")

# EL programa ejecuta la orden dependienco de el orden en el que coloquemos los if, elif y else. 
# Por eso es importante colocar primero las condiciones que no se quieren lograr 
# (en este caso, ser menor de edad) 
# y luego las condiciones que se quieren lograr (ser adulto o adulto mayor). 
# De esta manera, el programa ejecutará la orden correcta dependiendo de la edad ingresada por el usuario.