class Casa:
    def __init__(self, tipo, habitaciones, banos, metros_cuadrados, direccion, ciudad, estado, codigo_postal, precio, ano_construccion, piscina, jardin, garaje, chimenea, aire_acondicionado):
        self.tipo = tipo
        self.habitaciones = habitaciones
        self.banos = banos
        self.metros_cuadrados = metros_cuadrados
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        self.codigo_postal = codigo_postal
        self.precio = precio
        self.ano_construccion = ano_construccion
        self.piscina = piscina
        self.jardin = jardin
        self.garaje = garaje
        self.chimenea = chimenea
        self.aire_acondicionado = aire_acondicionado

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}")
        print(f"Habitaciones: {self.habitaciones}")
        print(f"Baños: {self.banos}")
        print(f"Metros Cuadrados: {self.metros_cuadrados}")
        print(f"Dirección: {self.direccion}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Estado: {self.estado}")
        print(f"Código Postal: {self.codigo_postal}")
        print(f"Precio: ${self.precio}")
        print(f"Año de Construcción: {self.ano_construccion}")
        print(f"Piscina: {'Sí' if self.piscina else 'No'}")
        print(f"Jardín: {'Sí' if self.jardin else 'No'}")
        print(f"Garaje: {'Sí' if self.garaje else 'No'}")
        print(f"Chimenea: {'Sí' if self.chimenea else 'No'}")
        print(f"Aire Acondicionado: {'Sí' if self.aire_acondicionado else 'No'}")

def main():
    casa1 = Casa("Apartamento", 3, 2, 120, "Romulo Gallegos 3625", "Caracas", "Distrito Federal", "1010", 150000, 2010, False, True, True, False, True)
    casa2 = Casa("Casa", 4, 3, 250, "El Rosal Av. Principal", "Caracas", "Distrito Federal", "1020", 300000, 2005, True, True, True, True, True)

    while True:
        print("\nMenu:")
        print("1. Elegir Casa 1")
        print("2. Elegir Casa 2")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            print("\nInformación de la Casa 1:")
            casa1.mostrar_info()
        elif opcion == "2":
            print("\nInformación de la Casa 2:")
            casa2.mostrar_info()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
