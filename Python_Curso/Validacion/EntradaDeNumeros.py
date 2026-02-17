# La función ahora utiliza una sola línea para verificar si la entrada no está vacía y si es un número. 
# La expresión entrada.replace('.', '', 1).isdigit() permite que se acepte un solo punto decimal, 
# lo que es útil para números decimales.

def es_numero_valido(entrada):
    return entrada.strip() != "" and entrada.replace('.', '', 2).isdigit()

while True:
    entrada = input("Por favor, ingresa un número (entero o decimal): ")
    
    if es_numero_valido(entrada):
        numero = float(entrada)  # Convertir la entrada a un número
        print(f"Número válido ingresado: {numero}")
        break  # Salir del ciclo si la entrada es válida
    else:
        print("¡Alerta! Solo se aceptan números y no se permiten entradas vacías. Intenta de nuevo.")

