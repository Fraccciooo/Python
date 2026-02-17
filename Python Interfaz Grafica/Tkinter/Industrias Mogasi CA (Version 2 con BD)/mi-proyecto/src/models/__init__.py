class Venta:
    def __init__(self, numero_factura, sucursal, fecha, total):
        self.numero_factura = numero_factura
        self.sucursal = sucursal
        self.fecha = fecha
        self.total = total

class Sucursal:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

# Aquí se pueden agregar más modelos según sea necesario.