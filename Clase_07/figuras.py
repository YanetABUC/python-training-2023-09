"""
Crear clases de diversas figuras geométricas (como "Circulo", "Cuadrado", "Triangulo") y 
usar polimorfismo para implementar un método "calcular_area()" en cada una de ellas. 
Crear una lista de figuras y calcular y mostrar el área de todas ellas utilizando este método.

"""
import math

class Figura:
    def __init__(self, medida) -> None:
        self.__medida = medida

    @property
    def medida(self):
        return self.__medida
    
    def calcular_area(self):
        pass

    def print_area(self):
        return f"El area es {self.calcular_area()}"


class Circulo(Figura):
    def __init__(self, radio) -> None:
        super().__init__(radio)

    def calcular_area(self):
        return math.pi * self.medida ** 2
    
    def print_area(self):
        return "Circulo: " + super().print_area()
    

class Cuadrado(Figura):
    def __init__(self, lado) -> None:
        super().__init__(lado)

    def calcular_area(self):
        return self.medida ** 2
    
    def print_area(self):
        return "Cuadrado: " + super().print_area()
    
class Triangulo(Figura):
    def __init__(self, base, altura) -> None:
        super().__init__(base)
        self.__altura = altura

    def calcular_area(self):
        return self.medida * self.__altura / 2
    
    def print_area(self):
        return "Triangulo: " + super().print_area()
    

figuras = [Circulo(20), Cuadrado(10), Triangulo(5, 10)]

for fig in figuras:
    print(fig.print_area())
