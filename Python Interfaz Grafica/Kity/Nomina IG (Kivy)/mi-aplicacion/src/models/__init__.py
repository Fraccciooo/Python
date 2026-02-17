class Empleado:
    def __init__(self, nombre, cedula, id, cargo, sueldo):
        self.nombre = nombre
        self.cedula = cedula
        self.id = id
        self.cargo = cargo
        self.sueldo = sueldo

    def validar_datos(self):
        if not self.nombre or not self.cedula or not self.cargo or self.sueldo < 0:
            return False
        return True

    def __repr__(self):
        return f'Empleado(ID: {self.id}, Nombre: {self.nombre}, Cédula: {self.cedula}, Cargo: {self.cargo}, Sueldo: {self.sueldo})'