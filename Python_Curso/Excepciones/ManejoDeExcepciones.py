# En este apartado se trata de entender todo la relacionado con las entradas invalidas
# se mejoran mediante la incorporacion de resultados optenidos por la consola
# dichos resultados son errados, por lo tanto, con las exceptiones, se manejan con tranquilidad
# esos errores (numericos, caracteres, espacioes vacios, etc...)

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
