class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print(f"El perro {self.nombre} esta ladrando")

class Gato(Animal):
    def hablar(self):
        print(f"El gato {self.nombre} esta maullando")

animales = [Perro("Firulais"), Gato("Garfield")]

for animal in animales:
    animal.hablar()