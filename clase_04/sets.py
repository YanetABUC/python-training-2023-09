numeros = {1, 2, 3, 4}
letras = set(["a", "b", "c"])

print(numeros)
print(letras)

#union
print( numeros | letras )
print(numeros.union(letras))

#interseccion
print( numeros & letras )
print(numeros.intersection(letras))

#diferencia
print( numeros - letras )
print(numeros.difference(letras))