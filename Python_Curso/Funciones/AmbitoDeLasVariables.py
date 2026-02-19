variable_global = "Soy global pa..."

def mostrar():
    # En esta funcion el valor de "nombre", se almacena solo en esta funcion
    # debido a que es una variable local, es decir, solo existe dentro de esta funcion
    nombre = "Ignacio"
    print(nombre)
    print(variable_global) # Se muestra el valor de la variable global, que es "Soy global pa..."

mostrar() # Se muestra el valor de la variable nombre, que es "Ignacio"

# Ahora bien, una variable global se puede usar tanto en una funcion como en 
# cualquier parte del codigo, es decir, su valor se almacena en la memoria 
# y se puede acceder a ella desde cualquier parte del codigo.

print(variable_global) # Se muestra el valor de la variable global, que es "Soy global pa..."
print(variable_global)
print(variable_global)
print(variable_global)