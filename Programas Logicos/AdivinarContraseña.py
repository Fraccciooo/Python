import string
import time

caracteres = string.ascii_lowercase + string.digits  # Solo letras minúsculas y números

def generar_contraseñas(caracteres, longitud):
    
    if longitud == 0:
        yield ''
    else:
        for caracter in caracteres:
            for subcontraseña in generar_contraseñas(caracteres, longitud - 1):
                yield caracter + subcontraseña
                  
def fuerza_bruta_contraseña(contraseña_objetivo):
    longitud_maxima = len(contraseña_objetivo)  # Longitud máxima igual a la longitud de la contraseña objetivo
    intentos = 0  # Contador de intentos

    for longitud in range(1, longitud_maxima + 1):
        for candidato in generar_contraseñas(caracteres, longitud):
            intentos += 1
            if candidato == contraseña_objetivo:
                return candidato, intentos
            
    return None, intentos

# Solicitar al usuario que ingrese la contraseña
contraseña_objetivo = input("Ingresa la contraseña a adivinar (exactamente 5 caracteres): ")

# Medir el tiempo de ejecución
inicio_tiempo = time.time()
resultado, intentos = fuerza_bruta_contraseña(contraseña_objetivo)
fin_tiempo = time.time()

if resultado:
    print(f"Contraseña encontrada: {resultado} en el intento #{intentos}")
    print(f"Tiempo transcurrido: {fin_tiempo - inicio_tiempo:.2f} segundos")
else:
    print(f"Contraseña no encontrada después de {intentos} intentos")
    print(f"Tiempo transcurrido: {fin_tiempo - inicio_tiempo:.2f} segundos")
