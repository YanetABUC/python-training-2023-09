frutas = ["aa", "bb", "cc"]
frutas.append("dd")
print(frutas)
sub_frutas = ["a1", "a2"]
frutas.append(sub_frutas)
print(frutas)

frutas2 = ["ee", "ff", "gg"]

frutas.extend(frutas2) #agregar iterables
print(frutas)

cadena = "verduras"
frutas.extend(cadena)
print(frutas)

frutas.insert(-1, "aqui")
frutas.insert(-100, "aqui2")
frutas.insert(100, "aqui3")
print(frutas)

frutas.remove("aa")
print(frutas)

print(frutas.pop())
print(frutas.pop(0))
print(frutas.pop(-1))
print(frutas)
