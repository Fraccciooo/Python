# La funcion "RETURN" se utiliza para poder jugar con un valor y devolverlo una vez se haya
# modificado o mejorado dicho valor

def multiplicar(x, y):
    resultado = x * y
    return resultado

x = int(input("Digite el valor de (x): "))
y = int(input("Digite el valor de (y): "))
operacion = multiplicar(x, y)

print(operacion) 