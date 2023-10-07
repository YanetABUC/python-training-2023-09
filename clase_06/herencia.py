class Animal:
    def __init__(self, nombre) -> None:
        self.nomber = nombre

    def hablar(self):
        print("El animal esta hablando")


class Perro(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    
    def hablar(self):
        super().hablar()
        print("El perro esta ladrando")

mi_animal = Animal("Gato")
mi_animal.hablar()

mi_perro = Perro("Firulais")
mi_perro.hablar()
