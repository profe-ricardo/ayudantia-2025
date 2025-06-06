"""
    Ejercicios listas - arreglos
"""

# Ejercicio 1: Lista de compras

lista_supermercado = [ 'Pan', 'Leche', 'Queso' ]
#print(lista_supermercado)

lista_supermercado.insert(1, 'Mantequilla')
#print(lista_supermercado)

lista_supermercado.pop(1) # Borra aquello en la ubicación indicada, por default es el último
lista_supermercado.remove('Leche') # Borra el primer resultado de la coincidencia
# print(lista_supermercado)

# Ejercicio 2: Mochila para clases

mochila_clases = [ 'Estuche', 'Cuaderno', 'Lapices', 'Libros' ]
#print(mochila_clases)

item_eliminado = mochila_clases.pop(1) # Saca Cuaderno
#print(mochila_clases)
#print('Item sacado:', item_eliminado)
mochila_clases.insert(1, 'Lonchera')
#print(mochila_clases)

mochila_clases.append('Zapatillas')
#print(mochila_clases)

# Ejercicio 3 - Películas por ver

peliculas_pendientes = [ 'Titanic', 'John Wick', 'Cars' ]
print(peliculas_pendientes)
print(f'Faltan {len(peliculas_pendientes)} películas por ver')

# peliculas_pendientes.remove('Cars')
# peliculas_pendientes.remove('Titanic')

# print(f'Faltan {len(peliculas_pendientes)} películas por ver')

for i in range(len(peliculas_pendientes)):
    print(f"Falta {peliculas_pendientes[i]} por ver")

for elemento in peliculas_pendientes:
    print(elemento)