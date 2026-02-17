def mostrar_factura(carrito, numero_factura, fecha, sucursal):
    if not carrito:
        print("\nNo hay productos registrados.")
        return
    
    print("\n" + "=" * 65)
    print(f"{'FACTURA DE VENTA':^65}")
    print("=" * 65)
    print(f"Número de Factura: {numero_factura}")
    print(f"Fecha: {fecha.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Sucursal: {sucursal}")
    print("-" * 65)
    print(f"{'Producto':<25}{'Precio Unit.':<12}{'Unidades':<12}{'Subtotal':>15}")
    print("-" * 65)
    
    total = 0
    for codigo, detalles in carrito.items():
        nombre = detalles['nombre']
        precio = detalles['precio']
        unidades = detalles['unidades']
        subtotal = precio * unidades
        
        print(f"{nombre:<25}${precio:<11.2f}{unidades:<12}${subtotal:>14.2f}")
        total += subtotal
    
    print("-" * 65)
    print(f"{'TOTAL:':<49}${total:>14.2f}")
    print("-" * 65)