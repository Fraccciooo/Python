

try:
    numerador = int(input("Ingrese un numero: "))
    denominador = int(input("Ingrese otro numero: "))
    resultado = numerador / denominador

except ZeroDivisionError as e:
    print(f"Error: {e}")
    print("Error: Division por cero no permitida.")
except ValueError as e:
    print(f"Error: {e}")
    print("Error: Entrada no valida. Por favor, ingrese numeros enteros.")
else:
    print(f"El resultado de {numerador} dividido por {denominador} es: {resultado}")
