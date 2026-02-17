from datetime import datetime

productos = {
    '1': {'nombre': 'Pan de Sandwich', 'precio': 0, 'unidades': 0},
    '2': {'nombre': 'Tequeños de 12', 'precio': 0, 'unidades': 0},
    '3': {'nombre': 'Tequeños de 24', 'precio': 0, 'unidades': 0},
    '4': {'nombre': 'Tequeños de 36', 'precio': 0, 'unidades': 0},
    '5': {'nombre': 'Empanaditas de Queso', 'precio': 0, 'unidades': 0},
    '6': {'nombre': 'Masa de Hojaldre 1 kg', 'precio': 0, 'unidades': 0},
    '7': {'nombre': 'Palmeritas', 'precio': 0, 'unidades': 0},
    '8': {'nombre': 'Pan Molido', 'precio': 0, 'unidades': 0},
    '9': {'nombre': 'Crotones', 'precio': 0, 'unidades': 0},
    '10': {'nombre': 'Mini tostadas', 'precio': 0, 'unidades': 0},
    '11': {'nombre': 'Pan de Perro Caliente', 'precio': 0, 'unidades': 0},
    '12': {'nombre': 'Pan de Hamburguesa', 'precio': 0, 'unidades': 0}
}

carrito = {}
facturas = []

sucursales = [
    "Gama Plus",    
    "Gama La India",
    "Gama Macaracuay",
    "Gama La Guairita",
    "Central Madeirense La Alameda",
    "Central Madeirense Santa Marta",
    "Central Madeirense Flor de Macaracuay",
    "Rio La Candelaria",
    "Rio La Trinidad",
    "Plaza El Paraiso",
    "Hiperparamo El Hatillo",
    "Paramo Palo Verde",
    "Paramo La Trinidad"
]