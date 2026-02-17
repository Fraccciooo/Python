import os 
from productos import productos, carrito, facturas, sucursales
from factura import mostrar_factura
from datetime import datetime
from menu import mostrar_menu
from limpiador import limpiar_y_pausar_pantalla

def mostrar_sucursales():
    print("\n=== SUCURSALES DISPONIBLES ===")
    for i, sucursal in enumerate(sucursales, 1):
        print(f"{i}. {sucursal}")

def registrar_productos():
    os.system("cls")
    print("\n=== REGISTRO DE PRODUCTOS ===")
    
    # Solicitar número de factura
    while True:
        try:
            numero_factura = input("\nIngrese el número de factura: ")
            # Verificar si el número de factura ya existe
            if any(f['numero'] == numero_factura for f in facturas):
                print("Error: Este número de factura ya existe.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número de factura válido.")
    
    # Selección de sucursal
    mostrar_sucursales()
    while True:
        try:
            opcion_sucursal = int(input("\nSeleccione el número de la sucursal (1-12): "))
            if 1 <= opcion_sucursal <= len(sucursales):
                sucursal = sucursales[opcion_sucursal - 1]
                break
            else:
                print("Por favor seleccione una sucursal válida.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    print("\nPor favor, registre todos los productos (use 0 si no hubo ventas)")
    
    carrito.clear()  # Limpiar el carrito para nueva venta
    for codigo, producto in productos.items():
        print(f"\nProducto: {producto['nombre']}")
        while True:
            try:
                precio = float(input("Ingrese el precio unitario: $"))
                unidades = int(input("Ingrese la cantidad de unidades vendidas: "))
                
                if precio < 0 or unidades < 0:
                    raise ValueError("Los valores no pueden ser negativos")
                
                carrito[codigo] = {
                    'nombre': producto['nombre'],
                    'precio': precio,
                    'unidades': unidades
                }
                
                subtotal = precio * unidades
                print(f"Registrado: {producto['nombre']}")
                print(f"Precio unitario: ${precio:.2f}")
                print(f"Unidades: {unidades}")
                print(f"Subtotal: ${subtotal:.2f}")
                print("-" * 40)
                break
                
            except ValueError as e:
                print(f"Error: {str(e) if str(e) else 'Por favor ingrese valores válidos.'}")
                limpiar_y_pausar_pantalla()
                
    fecha_actual = datetime.now()
    
    # Guardar la factura
    facturas.append({
        'numero': numero_factura,
        'fecha': fecha_actual,
        'sucursal': sucursal,
        'productos': carrito.copy()
    })
    
    # Mostrar la factura generada
    mostrar_factura(carrito, numero_factura, fecha_actual, sucursal)
    limpiar_y_pausar_pantalla()

def ver_facturas_anteriores():
    if not facturas:
        print("\nNo hay facturas registradas.")
        return

    os.system("cls")
    print("\n" + "=" * 65)
    print("\n=== FACTURAS REGISTRADAS ===")
    for factura in facturas:
        mostrar_factura(
            factura['productos'],
            factura['numero'],
            factura['fecha'],
            factura['sucursal']
        )
        print("\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "4":
            print("¡Gracias por usar el sistema!")
            break
        elif opcion == "1":
            registrar_productos()
        elif opcion == "2":
            if carrito:
                mostrar_factura(carrito, "ACTUAL", datetime.now(), "")
            else:
                print("\nNo hay una venta activa.")
        elif opcion == "3":
            ver_facturas_anteriores()
        else:
            print("\nOpción no válida. Por favor intente de nuevo.")

if __name__ == "__main__":
    print("Bienvenido al Sistema de Registro de Productos de Panadería")
    main()
    os.system("cls")