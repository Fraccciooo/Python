# Estructuras que almacenan los elementos similares a las listas
# los elementos de los sets son unicos, no se repiten
# son desordenados y no se modifican
# Si agregamos mas de una vez algun implemento, no se muestra las otras veces, solo una vez

implementos = {"Tenedor", "Cuchara", "Cuchillo"}
vasos = {"Grande", "Pequeño", "Mediano"}

implementos.add("plato") # Agrega un nuevo elemento de manera desordenada
implementos.remove("Tenedor") # Elimina un elemento 
implementos.pop() # Elimina un valor cualquiera, no se especifica
implementos.update(vasos) # Inser el Set de vasos en implementos

for i in implementos:
    print(i) # Al imprimirlo, no se muestran en orden, se muestran como quiera la computadora

