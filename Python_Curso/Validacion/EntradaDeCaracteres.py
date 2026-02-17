#----------
# Manera #1
#----------

while True:
    try:
        entrada = input("Introduce un texto: ")
        if not entrada:
            raise ValueError("No se aceptan entradas vacías.")
        elif not entrada.isalpha():
            raise ValueError("Solo se permiten caracteres alfabéticos.")
        else:
            print(f"Entrada válida: {entrada}")
            break;
    except ValueError as e:
        print(e)

#----------
# Manera #2
#----------

def validar_entrada(entrada):
    if not entrada.strip():
        raise ValueError("¡Alerta! No se aceptan entradas vacías.")
    if any(char.isdigit() for char in entrada):
        raise ValueError("¡Alerta! No se aceptan números.")

while True:
    entrada = input("Por favor, ingresa solo caracteres (sin números y sin espacios vacíos): ")
    try:
        validar_entrada(entrada)
        print(f"Entrada válida: {entrada}")
    except ValueError as e:
        print(e)