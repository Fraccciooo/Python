temperatura = int(input("¿Cual es la temperatura? "))

if temperatura == 0:
    print("Estas en 0 grados, ten cuidado")
elif temperatura > 30:
    print("Hace calor")
elif temperatura < 15:
    print("Hace frío")
elif temperatura >= 15 and temperatura <= 30:
    print("Hace una temperatura agradable")
else:
    print("Cualquier otro caso")
